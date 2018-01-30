
import BaseClass 

import Infrastructure.debug as debug

import numpy as np

class Connectable(BaseClass.BaseClass):
  """Extension to the base class for anything that can be connected to anything else. Still pretty generic I guess. :P """

  def __init__(self, *args, **kwargs):
    super(Connectable,self).__init__(**kwargs)
    
    #A Connector will be connected at two ends. Use a set to track what it's connected to
    self.connections=set()
    
    #Everything has resistance,even if it is zero
    self.resistance=0.0
    
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

  @debug.indent
  def getTheveninEquiv(self,excluded=[]):
    """ 
    Traverse the graph to determine the voltage of this node, and the output impedance 
    If excluded is specified as either an object or a iterable of objects connections that lead to these objects are ignored, to prevent cycles.
    
    """
    debug.verbose("Generating Thevenin equiv for",self)
    if not hasattr(excluded,"__iter__"):
      excluded=[excluded]
      
    connectedDevices=set(())
    
    conductance=0.0
    for connection in self.connections:
      debug.verbose("-At",self,"considering connection to",connection)
        
      if not connection in excluded:
        v,r=connection.getTheveninEquiv(excluded+[self])
        r+=connection.resistance
        debug.verbose("--Adding",v,r)
        connectedDevices.add( (v,r) )
        if r != 0.0:
          conductance+=1.0/r
        else:
          conductance+=np.inf  
      else:
        debug.verbose("--Connection Excluded")
              
    
    voltageNumerator=0
    voltageDenominator=0.0
    
    
    for device in connectedDevices: #For everything we're connected to
      resistanceProduct=1.0
      #print "Connection : ",device
      for v,r in connectedDevices.difference( set( [device] ) ): #Consider everything else as a voltage and resistance
        resistanceProduct*=r 
      voltageNumerator+=device[0]*resistanceProduct #Voltage times r
      voltageDenominator+=resistanceProduct

    outputVoltage=voltageNumerator/voltageDenominator
    outputResistance=1.0/conductance
    return outputVoltage,outputResistance
