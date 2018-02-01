from __future__ import print_function


from everyLine import EveryLine


class DebugLevels():
  silent = -1
  errors = 0
  warnings = 1
  verbose = 2


debugLevel = DebugLevels.verbose

""" If verboseObjectNames _repr__ includes the python id """
verboseObjectNames = True

__indent = -1

def alwaysDebug(level):
  def decorator(func):
    def wrapper(*args,**kwargs):
      global debugLevel
      oldLevel=debugLevel
      debugLevel=level
      x=func(*args,**kwargs)
      debugLevel=oldLevel
      return x
    return wrapper
  return decorator
    
def indented(func):
  def wrapper(*args, **kwargs):
    indent()
    x = func(*args, **kwargs)
    unindent()
    return x
  return wrapper

def indent(n=1):
  global __indent
  #print("+",n)
  __indent += n
  
def unindent(n=1):
  global __indent
  #print("-",n)
  __indent -= n
  
def __print(*args):
  global __indent
  #print("__indent is ", __indent)
  print("{0:>3}".format(__indent), ":", " |"*__indent, *args)


def verbose(*args, **kwargs):
  if debugLevel >= DebugLevels.verbose:
    __print(*args, **kwargs)
