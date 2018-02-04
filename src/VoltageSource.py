import BaseClasses.Connectable

import BaseClasses.Polarized


import Infrastructure.debug as debug
import Infrastructure.graph as graph
from Infrastructure.CircuitExceptions import ConnectionError


class VoltageSource(BaseClasses.Polarized.Polarized):
  """ Sets an absolute voltage between two points. Like a connector, but with two distinct ends"""

  def __init__(self, voltage, *args, **kwargs):
    super(VoltageSource, self).__init__(*args, **kwargs)
    self._voltage = voltage

  def _dotRepr(self):
    nodeName=self._dotName()+"_rect"
    
    entries=[]
    
    node=graph.dotEntry(nodeName)
    
    node['shape']='circle'
    node['label']=self.label+"\n"+str(self.voltage())+"V"
    entries.append(node)
    
    
    edge=graph.dotEntry( self._positiveConnection._dotName()+"--"+nodeName+":n" )
    edge['headlabel']="+"
    entries.append(edge)
    
    
    edge=graph.dotEntry( self._negativeConnection._dotName()+"--"+nodeName+":s" )
    edge['headlabel']="-"
    entries.append(edge)
    
    return entries
  
