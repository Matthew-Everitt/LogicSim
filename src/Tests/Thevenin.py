import VoltageSource
import resistor

import BaseClasses.AbsoluteVoltage as AbsoluteVoltage
import BaseClasses.Junction as Junction

import Infrastructure.debug as debug

#debug.debugLevel=debug.DebugLevels.errors

src=AbsoluteVoltage.AbsoluteVoltage(5)
gnd=AbsoluteVoltage.AbsoluteVoltage(0)

j=Junction.Junction(name="Output 1")
k=Junction.Junction(name="Output 2")


R=resistor.Resistor(1000,name="R1")

S=resistor.Resistor(2000,name="R2-1")
s=resistor.Resistor(2000,name="R2-2")

#T=resistor.Resistor(1000)
#U=resistor.Resistor(1000)



R.connect(src)
R.connect(j)

S.connect(j)
S.connect(gnd)

s.connect(j)
s.connect(gnd)

#T.connect(j)
#T.connect(k)

#U.connect(k)
#U.connect(gnd)
for _ in range(5):print
print j.getTheveninEquiv(j)

#print k.getTheveninEquiv(k)
