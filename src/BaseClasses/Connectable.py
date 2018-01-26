
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
    raise NotImplementedError( str(self)+" doesn't properly implement connect") 
