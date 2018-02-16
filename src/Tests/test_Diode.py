"""Tests designed to tset the behaviour of resistors"""

import unittest

import resistor
import Diode
import BaseClasses.Junction as Junction
import BaseClasses.AbsoluteVoltage as AbsoluteVoltage
import VoltageSource
import BaseClasses.VoltageProbe as VoltageProbe

class TestStringMethods(unittest.TestCase):

  def test_forwardBias(self):
    
    Vf=0.6
    Rf=10
    
    D=Diode.Diode(0.6,10)
    R=resistor.Resistor(1000000)
    
    gnd=AbsoluteVoltage.AbsoluteVoltage(0.0,name="gnd")
    
    j=Junction.Junction()
    
    #Vcc=VoltageSource.VoltageSource(5.0,name="Vcc")
    Vcc=AbsoluteVoltage.AbsoluteVoltage(5.0,name="Vcc")
    
    probe=VoltageProbe.VoltageProbe()
    
    
    #Vcc.connect(R,"positive")
    #Vcc.connect(gnd,"negative")
    Vcc.connect(R)
    
    R.connect(j)
    
    D.connect(j,"anode")
    D.connect(gnd,"cathode")
    
    probe.connect(j)
    

    print  probe.getVoltageResistance()
    #self.assertEqual(   (Vf,Rf) )

  def test_forwardBiasSeries(self):
    
    Vf=0.6
    Rf=10
    
    D1=Diode.Diode(Vf,Rf)
    D2=Diode.Diode(Vf,Rf)
    R=resistor.Resistor(  100000)
    
    gnd=AbsoluteVoltage.AbsoluteVoltage(0.0,name="gnd")
    
    j=Junction.Junction()
    k=Junction.Junction()
    #Vcc=VoltageSource.VoltageSource(5.0,name="Vcc")
    Vcc=AbsoluteVoltage.AbsoluteVoltage(5.0,name="Vcc")
    
    probe=VoltageProbe.VoltageProbe()
    
    
    #Vcc.connect(R,"positive")
    #Vcc.connect(gnd,"negative")
    Vcc.connect(R)
    
    R.connect(j)
    
    D1.connect(j,"anode")
    D1.connect(k,"cathode")
    
    D2.connect(k,"anode")    
    D2.connect(gnd,"cathode")
    
    probe.connect(j)
    
    import Infrastructure.graph as graph
    graph.graph(j).output("../junk/diode.gv")
    print  probe.getVoltageResistance()
    #self.assertEqual(   (Vf,Rf) )
 
  def test_reverseBias(self):
    D=Diode.Diode()
    R=resistor.Resistor(1000000)
    
    gnd=AbsoluteVoltage.AbsoluteVoltage(0.0,name="gnd")
    
    j=Junction.Junction()
    
    #Vcc=VoltageSource.VoltageSource(5.0,name="Vcc")
    Vcc=AbsoluteVoltage.AbsoluteVoltage(5.0,name="Vcc")
    
    probe=VoltageProbe.VoltageProbe()
    
    
    #Vcc.connect(R,"positive")
    #Vcc.connect(gnd,"negative")
    Vcc.connect(R)
    
    R.connect(j)
    
    D.connect(j,"cathode")
    D.connect(gnd,"anode")
    
    probe.connect(j)
    
    print probe.getVoltageResistance()
    
    
if __name__ == "__main__":
  
  import os,inspect
  import runTests
  
  currentFile=os.path.abspath(inspect.getfile(inspect.currentframe()))
  print currentFile
  runTests.runTests( start_dir=os.path.dirname(currentFile), glob=os.path.basename(currentFile) )
