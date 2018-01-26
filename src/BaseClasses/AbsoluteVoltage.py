import Connectable

import Junction

import Infrastructure.debug as debug


class AbsoluteVoltage(Junction.Junction):
  """ A node that's always at a fixed voltage, such as ground. Can also be used to provide, for example, a +5V supply if you don't want to mess around with voltage sources. """
  
  def __init__(self,voltage,*args,**kwargs):
    super(AbsoluteVoltage,self).__init__(*args,**kwargs)
    self.voltage=voltage
  
