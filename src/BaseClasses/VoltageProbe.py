import Connectable

import Junction

import Infrastructure.debug as debug

import numpy as np

class VoltageProbe(Junction.Junction):
  """ A node that asserts a voltage (to terminate chains) via an infinite resistance, so as to not alter the behaviour"""

  def __init__(self, *args, **kwargs):
    super(VoltageProbe, self).__init__(*args, **kwargs)

  @debug.indented
  def getTheveninEquiv(self, exclude=None):
    """ 
    The Thevenin equivalent of a source is ... the source.

    Returns two values, the effective voltage and resistance.
    """
    debug.verbose("Generating Thevenin equiv for", self, "- 0V via inf Ohms")
    return 0.0, np.inf

  def getVoltageResistance(self):
    return super(VoltageProbe,self).getTheveninEquiv()
  
  def _dotRepr(self):
    entries=super(VoltageProbe,self)._dotRepr()
    for e in entries:
      entries['shape']='house'
    return entries
