import sys

class EveryLine(object):
  """ Usage:
  with EveryLine(func):
    code()
    
  Runs func between every line of code(). Good for debugging
  """
  def __init__(self, func):
      self.func = func

  def __enter__(self):
      sys.settrace(self.func)
      return self

  def __exit__(self, ext_type, exc_value, traceback):
      sys.settrace(None)
