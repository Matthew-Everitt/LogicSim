#import numpy as np

import roles
import Infrastructure.graph as graph

class Resistor(roles.Connector):
  def __init__(self, r, *args, **kwargs):
    super(Resistor, self).__init__(*args, **kwargs)
    self._resistance = r
  
  def _dotRepr(self):
    nodeName=self._dotName()+"_rect"
    
    entries=[]
    
    node=graph.dotEntry(nodeName)
    
    node['shape']='rect'
    node['label']=self.label+"\n"+str(self.resistance())+"ohms"
    entries.append(node)
    
    for conn in self.connections:
      entries.append(graph.dotEntry( conn._dotName()+"--"+nodeName ))
    
    return entries
