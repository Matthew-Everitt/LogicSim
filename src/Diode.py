import BaseClasses.Connectable

import BaseClasses.Polarized


import Infrastructure.debug as debug
import Infrastructure.graph as graph
from Infrastructure.CircuitExceptions import ConnectionError


class Diode(BaseClasses.Polarized.Polarized):
  """ Sets an absolute voltage between two points. Like a connector, but with two distinct ends"""
  avaliableConnections= { 
    "anode":BaseClasses.Polarized.ConnectionID( "anode", "A", "w"),
    "cathode":BaseClasses.Polarized.ConnectionID("cathode","K","e")
                        }
  def __init__(self, Vf=0.6, Rf=10, Rr=1000000,  *args, **kwargs):
    super(Diode, self).__init__(*args, **kwargs)
    self._voltage = Vf
    self._Rf=Rf
    self._Rr=Rr

  def voltage(self,fromConnection=None,toConnection=None):
    if fromConnection is self.connectionMap["anode"] or fromConnection is None:
      return self._voltage
    else:
      return 0.0
    
  def resistance(self,fromConnection=None,toConnection=None):
    if fromConnection is self.connectionMap["anode"] or fromConnection is None:
      return self._Rf
    else:
      return self._Rr
  
  def _dotRepr(self):
    nodeName=self._dotName()+"_rect"
    
    entries=[]
    
    node=graph.dotEntry(nodeName)
    
    node['shape']='rarrow'
    node['label']=self.label+"\n"+str(self.voltage())+"V"
    entries.append(node)
    
    for name,description in self.avaliableConnections.iteritems():
      edge=graph.dotEntry( self.connectionMap[name]._dotName()+"--"+nodeName+":"+description.pole )
      edge['headlabel']=description.label
      entries.append(edge)
    
    
    return entries
  
