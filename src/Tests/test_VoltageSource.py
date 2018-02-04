import VoltageSource
import resistor
import BaseClasses.VoltageProbe as VoltageProbe
import BaseClasses.AbsoluteVoltage as AbsoluteVoltage
import BaseClasses.Junction as Junction

import Infrastructure.graph as graph


import unittest
class TestStringMethods(unittest.TestCase):

  def test_VoltageSource(self):
    V=VoltageSource.VoltageSource(5,name="SRC")

    gnd=AbsoluteVoltage.AbsoluteVoltage(0,name="gnd")
    probe=VoltageProbe.VoltageProbe(name="probe")

    V.connect(gnd,V.negative)
    V.connect(probe,V.positive)

    self.assertEqual( probe.getVoltageResistance(), (5.0,0.0) )
    
  def test_VoltageSourcePolarity(self):
    """ Test that a reverse connected voltage source gives a negative voltage. This currently doesn't work!"""
    V=VoltageSource.VoltageSource(5,name="SRC")

    gnd=AbsoluteVoltage.AbsoluteVoltage(0,name="gnd")
    probe=VoltageProbe.VoltageProbe(name="probe")

    V.connect(gnd,V.positive)
    V.connect(probe,V.negative)

    self.assertEqual( probe.getVoltageResistance(), (-5.0,0.0) )

  def test_TwoVoltageSources(self):
    V1=VoltageSource.VoltageSource(5,name="SRC")
    V2=VoltageSource.VoltageSource(5,name="SRC")
    
    gnd=AbsoluteVoltage.AbsoluteVoltage(0,name="gnd")
    probe=VoltageProbe.VoltageProbe(name="probe")

    j=Junction.Junction()

    V1.connect(gnd,V1.negative)
    V1.connect(j,V1.positive)
    
    V2.connect(j,V2.negative)
    V2.connect(probe,V2.positive)

    self.assertEqual( probe.getVoltageResistance(), (10.0,0.0) )
    
  def test_TwoVoltageSourcesWithResistor(self):
    V1=VoltageSource.VoltageSource(5,name="SRC")
    V2=VoltageSource.VoltageSource(5,name="SRC")
    
    R=resistor.Resistor(100)
    
    gnd=AbsoluteVoltage.AbsoluteVoltage(0,name="gnd")
    probe=VoltageProbe.VoltageProbe(name="probe")

    

    V1.connect(gnd,V1.negative)
    V1.connect(R,V1.positive)
    
    V2.connect(R,V2.negative)
    V2.connect(probe,V2.positive)
    graph.graph(R).output("test.gv")
    self.assertEqual( probe.getVoltageResistance(), (10.0,100.0) )

if __name__ == "__main__":
  
  import os,inspect
  import runTests
  
  currentFile=os.path.abspath(inspect.getfile(inspect.currentframe()))
  print currentFile
  runTests.runTests( start_dir=os.path.dirname(currentFile), glob=os.path.basename(currentFile) )
