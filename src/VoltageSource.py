import BaseClasses.Connectable

import BaseClasses.Polarized


import Infrastructure.debug as debug
from Infrastructure.CircuitExceptions import ConnectionError


class VoltageSource(BaseClasses.Polarized.Polarized):
  """ Sets an absolute voltage between two points. Like a connector, but with two distinct ends"""

  def __init__(self, voltage, *args, **kwargs):
    super(VoltageSource, self).__init__(*args, **kwargs)
    self.voltage = voltage
