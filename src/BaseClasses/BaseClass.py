from numpy import timedelta64 as interval
import Infrastructure.debug as debug


class BaseClass(object):
  """Base class for many things. Implements some basic common functionality that will typically be overwritten"""

  # Shared accross all initialisations, this records the number of times a certain name has been requested, so we can append something to it to ensure that it's unique.
  __usedNames = {}

  def __init__(self, name=None, label=None):
    """
    Base class for anything that we want to be able to name, or to add to a graph

    Parameters:
    name - A user friendly name for the object. If nothing is provided the name of the class is used. This is manipulated by appending a number to ensure uniqueness
    label - A label to be used for graphs etc. If none provided the (unmanipulated) name is used.

    """
    # Apply defaults if needed
    if not name:
      name = self.__class__.__name__

    if not label:
      label = name
    self.label = label

    # Ensure uniquness of name
    if self.__usedNames.has_key(name):
      self.name = name+'['+str(self.__usedNames[name])+']'
      self.__usedNames[name] += 1
    else:
      self.name = name
      self.__usedNames[name] = 1

    self._timeUntilEvent = interval(0, 's')

  def timeUntilEvent(self):
    """Should return the an np.timedelta64 specifying how long until the object will produce an update (0s if no update is expected)"""
    return self._timeUntilEvent

  def updateTime(self, timeStep):
    """Called by ... something to move timeforwards by the np.timedelta64 timeStep. This default implentation calls self.update(None), which should be fine for most things"""
    self._timeUntilEvent -= timeStep
    if self._timeUntilEvent <= interval(0, 's'):
      self._timeUntilEvent = interval(0, 's')
      self.update(None)

  def update(self, driver):
    pass

  def __repr__(self):
    """ returns "class :  name - 'label'". Should be enough to uniquely identify anything, but if not there's an option in debug.py 'verboseObjectNames' that also appends id(self) (in hex) like the default implementation"""
    return self.__class__.__name__+" :  "+self.name+" - '"+self.label+"'  "+(hex(id(self)) if debug.verboseObjectNames else "")

  def __str__(self):
    """Returns the label of the object, which should be enough to tell the user what the object is supposed to be in context"""
    return self.label

  def __dotName(self):
    return '"'+self.__repr__()+'"'
