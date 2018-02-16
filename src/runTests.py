import unittest
import coverage


import Infrastructure.debug as debug
debug.debugLevel = debug.DebugLevels.silent
#Find the filename of this file. Obviously we can't record ourselves hitting every line, so just omit this one file.
import os,inspect

def runTests(glob="*.py",start_dir="./Tests"):

  currentFile=inspect.getfile(inspect.currentframe())

  cov=coverage.Coverage(source=".", branch=True,omit=currentFile)


  loader = unittest.TestLoader()

  try:
    import colour_runner.runner
    runner=colour_runner.runner.ColourTextTestRunner(verbosity=10)
  except Exception as e:
    #print e
    runner = unittest.TextTestRunner(verbosity=10)
    
  cov.start() 

  suite = loader.discover(start_dir,pattern=glob)

  runner.run(suite)
  cov.stop()

  percentCovered=cov.html_report()
  print "Covered {0:.2f}% of the code".format(percentCovered)


if __name__ == "__main__":
  runTests()
