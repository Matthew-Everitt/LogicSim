from resistor import Resistor

# Totally worthwhile try..except blocks that really add something...
# Placeholder until I find / write a test framework of some kind, and work out what these tests are actually for.

try:
  r = Resistor(1e3, name="r")
  s = Resistor(1e3, name="s")
except Exception as e:
  raise e


try:
  r.connect(s)
except Exception as e:
  raise e
