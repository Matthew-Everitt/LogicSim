"""Tests designed to tset the behaviour of resistors"""

import unittest

import resistor
import BaseClasses.Junction as Junction
import BaseClasses.AbsoluteVoltage as AbsoluteVoltage

class TestStringMethods(unittest.TestCase):

  def twoResistorDivider(self,R1,R2,V):
    src = AbsoluteVoltage.AbsoluteVoltage(V,name="Vcc")
    gnd = AbsoluteVoltage.AbsoluteVoltage(0,name="GND")

    j = Junction.Junction(name="Output")

    R = resistor.Resistor(R1, name="R1")

    S = resistor.Resistor(R2, name="R2")



    R.connect(src)
    R.connect(j)

    S.connect(j)
    S.connect(gnd)
    
    
    import Infrastructure.graph
    Infrastructure.graph.graph(R).output("../junk/test.gv")
    
    return j.getTheveninEquiv()

    
  def test_EqualDivider(self):
    Vin=5
    Rin=1000
    
    Vout,Rout = self.twoResistorDivider( Rin, Rin, Vin)
    
    self.assertEqual( Vout, Vin/2.0)
    self.assertEqual( Rout, Rin/2.0)
    
  def test_UnequalDivider(self):
    Vin=5
    RinTop=3
    RinBottom=RinTop/2.0
    Vout,Rout = self.twoResistorDivider( RinTop, RinBottom, Vin)
    
    self.assertEqual( Vout, Vin/3.0)
    self.assertEqual( Rout, 1.0/(1.0/RinTop+1.0/RinBottom))
    
