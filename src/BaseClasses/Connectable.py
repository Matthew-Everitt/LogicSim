
import BaseClass 

class Connectable(BaseClass.BaseClass):
  """Extension to the base class for anything that can be connected to anything else. Still pretty generic I guess. :P """

  def __init__(self, *args, **kwargs):
    super(Connectable,self).__init__(**kwargs)
    
    #A Connector will be connected at two ends. Use a set to track what it's connected to
    self.connections=set()
    
    #Accept either a single iterable, or a list of things to connect to (or nothing, I suppose)
    if len(args) > 0:
      if len(args)==1 and hasattr("__iter__", args[0]):
        args=args[0]
        
      for connection in args:
        self.connect(connection)  
        

  def connect(self, connection):
    """ What you should allow connectons to depends heavily on what you are, so child classes need to implement this themselves. The only common requirement is that the object gets added to self.connections anyway."""
    raise NotImplementedError( str(self)+" doesn't properly implement connect") 
  
  def disconnect(self,connection):
    """ Simple disconnecter for set based lists of connections - the default"""
    if connection in self.connections:
      self.connections.remove(connection)
      connection.disconnect(self)
    else:
      if debug.debugLevel >= debug.debugLevels.Warning:
        print "Tried to remove ", connection, " from ", self, " but it wasn't connected"
