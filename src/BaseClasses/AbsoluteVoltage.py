import Connectable

import Junction

import Infrastructure.debug as debug


class AbsoluteVoltage(Junction.Junction):
  """ A node that's always at a fixed voltage, such as ground. Can also be used to provide, for example, a +5V supply if you don't want to mess around with voltage sources. """

  def __init__(self, voltage, *args, **kwargs):
    super(AbsoluteVoltage, self).__init__(*args, **kwargs)
    self.voltage = voltage

  @debug.indented
  def getTheveninEquiv(self, exclude=None):
    """ 
    The Thevenin equivalent of a source is ... the source.

    Returns two values, the effective voltage and resistance.
    """
    if debug.debugLevel >= debug.DebugLevels.verbose:
      debug.verbose("Generating Thevenin equiv for", self,
              "- fixed voltage of", self.voltage)
    return float(self.voltage), 0.0

    
  def _dotRepr(self):
    entries=super(AbsoluteVoltage,self)._dotRepr()
    for e in entries:
      entries['shape']='invhouse'
    return entries
