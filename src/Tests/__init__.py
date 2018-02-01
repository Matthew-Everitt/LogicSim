import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
  inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
if not parentdir in sys.path:
  sys.path.insert(0, parentdir)


#Suppress warnings on divide by zero / inf / nan - sometimes they're suppose to be there (voltage sources / probes etc)
#We also get an invalid error for 0.0/0.0, so ignore that too
import numpy 

numpy.seterr(divide="ignore",invalid="ignore")
