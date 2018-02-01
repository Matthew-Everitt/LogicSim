import Connectable

import Junction

import Infrastructure.debug as debug
import Infrastructure.graph as graph
from Infrastructure import CircuitExceptions


class Connector(Connectable.Connectable):
  """ Something that goes between two places to and causes their voltages to be related"""

  def connect(self, connection):
    """Connect one end of a connection to the object 'connection' """
    # Don't doubly connect. This doesn't prevent us from doing anything as the only real use case for that would be to connect both ends of the resistor to the same junction, which shorts out the resistor and so is not an important situation. If we do really want to short out a resistor for whatever reason we can use two junctions and a wire (or 0Ohm resistor)
    # In cases like that the thing in self.connections will be the junction, so this will pass by here anyway
    debug.verbose( "In ", self, ".connect(", connection, ")")

    if connection in self.connections:
      debug.verbose( self, "already connected to", connection)
      return

    # Resistors can only connect to two places. Those places should be junctions, which can connect to arbitrarily many things, but a resistor itself has two ends.
    if len(self.connections) == 2:
      raise CircuitExceptions.ConnectionError(
        "Connector "+str(self)+" cannot connect to more than two places.")

    # Ok, we want to connect. Great. How should we connect?

    # Connect directly to junctions, that's what they're for
    if isinstance(connection, Junction.Junction):
      self.connections.add(connection)
      connection.connect(self)
      return

    # We can connect to other Connectors, but we need to create a junction at which to do so
    if isinstance(connection, Connector):
      junc = Junction.Junction(
        self, connection, name="AutoGeneratedJunction", label="")
      return
    # If we reach this point then we haven't known how to connect to whatever it is, which means either somebody is trying to do something really weird, or we just haven't implemented that yet
    raise NotImplementedError("Don't know how to add a connection from "+str(
      connection)+" to "+str(self)+". Maybe try the other way around?")

  def _dotRepr(self):
    import itertools
    entries=[]
    for x,y in itertools.combinations(self.connections,2):
      entry = graph.dotEntry(definition=x._dotName()+"--"+y._dotName())
      entry['label']=self.label
      entries.append(entry)
    return entries
