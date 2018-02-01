import unittest
import coverage

#Find the filename of this file. Obviously we can't record ourselves hitting every line, so just omit this one file.
import os,inspect
currentFile=inspect.getfile(inspect.currentframe())

cov=coverage.Coverage(source=".", branch=True,omit=currentFile)

        

loader = unittest.TestLoader()
start_dir = './Tests'

try:
  import colour_runner.runner
  runner=colour_runner.runner.ColourTextTestRunner()
except Exception as e:
  print e
  runner = unittest.TextTestRunner()
  
cov.start() 

suite = loader.discover(start_dir,pattern="*.py")

runner.run(suite)
cov.stop()

percentCovered=cov.html_report()
print "Covered {0:.2f}% of the code".format(percentCovered)
