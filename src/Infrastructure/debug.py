from enum import Enum

from everyLine import EveryLine

  
class DebugLevels():
  silent    = -1
  errors    =  0
  warnings  =  1
  verbose   =  2
  
debugLevel =  DebugLevels.verbose

""" If verboseObjectNames _repr__ includes the python id """
verboseObjectNames = True
