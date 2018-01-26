from VoltageSource import VoltageSource

from resistor import Resistor

v=VoltageSource(1)
r=Resistor(2)
s=Resistor(12)


v.connect(r,v.positive)
v.connect(s,v.negative)
r.connect(s)
