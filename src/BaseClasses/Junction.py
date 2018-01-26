import Connectable

import Connector

import Infrastructure.debug as debug


class Junction(Connectable.Connectable):
  """ A place where an arbitrary number of Connectors meet """
  def connect(self,connection):
    """Connect something to the junction. This is a lot like a Connector, but there is no limit on the number of things, and the rule Connector -> junction is of course reversed here."""
    if connection in self.connections:
      if debug.debugLevel >= debug.DebugLevels.verbose:
        print self,"already connected to",connection
        return

    #Connect directly to connections, that's the name of the game.
    if isinstance(connection, Connector.Connector):
      self.connections.add(connection)
      connection.connect(self)
      return
    
    #We can connect to other Junctions (even if that is a bit pointless, it might end up making some circuits neater), but we need to create a connection to go between them.
    if isinstance(connection, Junction):
      
      conn=Connector.Connector( connection, self, name="AutoGeneratedConnection")
      #Hopefully that constructor has done everything needed
      return
    
    #If we reach this point then we haven't known how to connect to whatever it is, which means either somebody is trying to do something really weird, or we just haven't implemented that yet
    raise NotImplementedError( "Don't know how to add a connection from "+str(connection)+" to "+str(self) )
