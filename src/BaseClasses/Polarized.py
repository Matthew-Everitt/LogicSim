import Connectable

import Device
import Connector
import Junction


import BaseClasses.BaseClass as BaseClass

import Infrastructure.debug as debug
from Infrastructure.CircuitExceptions import ConnectionError

class ConnectionID(BaseClass.BaseClass):
  def __init__(self, name, label="", pole=""):
    """ Name is the name of the connection, label is the symbol used on graphical representations, and pole is a helper for dot, the compass point the connection would normally appear on on a schematic (-ve on south, +ve on north for a src, for example)"""
    super(ConnectionID,self).__init__(name,label)
    self.pole=pole

class Polarized(Connector.Connector, Device.Device):
  """ Like a connector, but with two distinct ends"""
  
  
  avaliableConnections={}

  def __init__(self, *args, **kwargs):
    super(Polarized, self).__init__(*args, **kwargs)
    self.connectionMap={}
        

                        
  def connect(self, connection, connectionName=None):
    """A voltage source has two special connections, +ve and negative. As such this function should never be called by anything but the end user, who should probably only call it via a helper or init function anyway"""
    debug.verbose( "In ", self, ".connect(", connection, ", ",connectionName,")")
    debug.indent()
    debug.verbose("Has connections :  ",self.connections)
    debug.unindent()
    
    if isinstance(connectionName , str):
      try:
        conenctionName=self.avaliableConnections[connectionName]
      except KeyError:
        raise ConnectionError(str(self)+" does not have a connection \""+connectionName+"\"")
      
    
    # Check to see if we're already connected
    if connection in self.connections:
      debug.verbose( self, "already connected to", connection)
      # If we're already connected to the same polarity (or if we've not been told which polarity) then assume we're ok to leave it as is. This is mainly so the reverse connection is gracefully ignored
      if connectionName is None:
        return
      
      
      if self.connectionMap[connectionName] != connection:
        # Not just trying to reconnect, trying to short us out or similar. Bad times.
        raise ConnectionError("Trying to connect "+str(connection)+" to "+str(self)+", but that looks like it would be a short!")
      return

    #Not already connected, no name specified, what can we do?
    if connectionName is None:
      raise ConnectionError("Tried to connected to a polarized device without specifying a polarity.")

    # Connect directly to connections, that's the name of the game.
    if isinstance(connection, Junction.Junction):
      self.connectionMap[connectionName]=connection
      # Also maintain the standard connection system
      self.connections.add(connection)
      connection.connect(self)
      return

    # We can connect to other Connectors, but we need to create a junction at which to do so
    if isinstance(connection, Connector.Connector):
      junc = Junction.Junction(name="AutoGeneratedJunction")
      connection.connect(junc)
      self.connect(junc, connectionName)
      return
    # If we reach this point then we haven't known how to connect to whatever it is, which means either somebody is trying to do something really weird, or we just haven't implemented that yet
    raise NotImplementedError("Don't know how to add a connection from "+str(connection)+" to "+str(self))

