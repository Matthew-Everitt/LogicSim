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


def indent(func):
  def wrapper(*args, **kwargs):
    global __indent
    __indent += 1
    x = func(*args, **kwargs)
    __indent -= 1
    return x
  return wrapper


def __print(*args):
  global __indent
  #print("__indent is ", __indent)
  print(__indent, ":", " |"*__indent, *args)


def verbose(*args, **kwargs):
  if debugLevel >= DebugLevels.verbose:
    __print(*args, **kwargs)
