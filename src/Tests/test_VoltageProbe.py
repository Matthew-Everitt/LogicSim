"""Tests designed to tset the behaviour of resistors"""

import unittest

import resistor
import BaseClasses.Junction as Junction
import BaseClasses.AbsoluteVoltage as AbsoluteVoltage
import BaseClasses.VoltageProbe as VoltageProbe
class TestStringMethods(unittest.TestCase):

  def test_ProbeInfluence(self):
    src = AbsoluteVoltage.AbsoluteVoltage(5,name="Vcc")
    gnd = AbsoluteVoltage.AbsoluteVoltage(0,name="GND")

    probe=VoltageProbe.VoltageProbe()

    j = Junction.Junction(name="Joint")

    R = resistor.Resistor(1000, name="R1")

    S = resistor.Resistor(1000, name="R2")



    R.connect(src)
    R.connect(j)

    S.connect(j)
    S.connect(gnd)
    
    before = j.getVoltageResistance()
    
    probe.connect(j)
    
    after = j.getVoltageResistance()
    
    #self.assertEqual ( before, after )
    
    
  def test_ProbeReturnsCorrectValue(self):
    src = AbsoluteVoltage.AbsoluteVoltage(5,name="Vcc")
    gnd = AbsoluteVoltage.AbsoluteVoltage(0,name="GND")
    
    probe=VoltageProbe.VoltageProbe()

    j = Junction.Junction(name="Joint")

    R = resistor.Resistor(1000, name="R1")

    S = resistor.Resistor(1000, name="R2")



    R.connect(src)
    R.connect(j)

    S.connect(j)
    S.connect(gnd)
    
    probe.connect(j)
    
    
    atJ= j.getVoltageResistance()

    atProbe = probe.getVoltageResistance()
    
    #self.assertEqual ( atJ, atProbe)
