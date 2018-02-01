
import BaseClass

import Infrastructure.debug as debug

import numpy as np


class Connectable(BaseClass.BaseClass):
  """Extension to the base class for anything that can be connected to anything else. Still pretty generic I guess. :P """

  def __init__(self, *args, **kwargs):
    super(Connectable, self).__init__(**kwargs)

    # A Connector will be connected at two ends. Use a set to track what it's connected to
    self.connections = set()

    # Everything has resistance,even if it is zero
    self.resistance = 0.0

    # Accept either a single iterable, or a list of things to connect to (or nothing, I suppose)
    if len(args) > 0:
      if len(args) == 1 and hasattr("__iter__", args[0]):
        args = args[0]

      for connection in args:
        self.connect(connection)

  def connect(self, connection):
    """ What you should allow connectons to depends heavily on what you are, so child classes need to implement this themselves. The only common requirement is that the object gets added to self.connections anyway."""
    raise NotImplementedError(
      str(self)+" doesn't properly implement connect")

  def disconnect(self, connection):
    """ Simple disconnecter for set based lists of connections - the default"""
    if connection in self.connections:
      self.connections.remove(connection)
      connection.disconnect(self)
    else:
      debug.warning("Tried to remove ", connection, " from ", self, " but it wasn't connected.")

  @debug.indented
  def getTheveninEquiv(self, excluded=[]):
    """ 
    Traverse the graph to determine the voltage of this node, and the output impedance 
    If excluded is specified as either an object or a iterable of objects connections that lead to these objects are ignored, to prevent cycles.

    """
    debug.verbose("Generating Thevenin equiv for", self)

    # Make sure excluded is iterable
    if not hasattr(excluded, "__iter__"):
      excluded = [excluded]

      # Keep track of the properties of what we're connected to in a set.
    connectedDevices = set(())

    # We can tot up the total conductance easily
    conductance = 0.0

    # i is a counter that we can use to ensure that every connection is unique. This is needed as we're using a  set, which really simplifies the calculation at the end, but has the problem that if multiple connections return the same properties all but the first are ignored
    i = 0

    # Follow every link
    for connection in self.connections:
      debug.verbose("-At", self, "considering connection to", connection)

      if not connection in excluded:
        # If we've not been told to exclude it follow the link to a simplified source.
        v, r = connection.getTheveninEquiv(excluded+[self])
        # Add the resistance of this link. Everything has a resistance, and it's zero if it hasn't been explicitly set, so we can do this without worrying if it makes any particular physical sense or not
        r += connection.resistance
        debug.verbose("--Adding", v, "V via", r, "Ohms")
        # Add the result (and the counter) to the set of connections
        connectedDevices.add((v, r, i))

        # If the resistance of the source is non zero add its reciprocal (the conductance) to the accumulator
        if r != 0.0:
          conductance += 1.0/r
        else:
          # If the resistance is zero then the conductance is infinite.
          conductance += np.inf
      else:
        debug.verbose("--Connection Excluded")
      debug.verbose("Connection list :  ", connectedDevices)
      i += 1

    voltageNumerator = 0
    voltageDenominator = 0.0

    # Calculate the equivalent voltage:
    #   V1*R2..Rn + V2*R1R3..Rn + ... Vn*R1..R[n-1]
    # V=  ___________________________________________
    #     R2R3..Rn + R1R3..Rn + ... + R1R2..R[n-1]

    for device in connectedDevices:  # For everything we're connected to
      resistanceProduct = 1.0
      # Find the product of all the other resistances. This is why we use a set, it's really easy to get the list of everything that isn't the current connection
      # Consider everything else as a voltage and resistance
      for v, r, _ in connectedDevices.difference(set([device])):
        resistanceProduct *= r

      # We can sum the two parts of the fraction and divide at the end.
      voltageDenominator += resistanceProduct
      voltageNumerator += device[0]*resistanceProduct

    # And now the results are easy to get
    outputVoltage = voltageNumerator/voltageDenominator
    outputResistance = 1.0/conductance
    return outputVoltage, outputResistance
