#import numpy as np

import roles

class Resistor(roles.Connector):
  def __init__(self, r,  *args, **kwargs):
    super(Resistor,self).__init__(*args,**kwargs)
    self.resistance=r
    
        
