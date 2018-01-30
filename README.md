# LogicSim
A very basic attempt at a voltage driven logic IC simulation.

So far all that's been decided is that there are three main types of 'thing', connectors, that go between two points, junctions where connectors meet, and 'other', where other things happen (voltages are set and measured, for example)

I'm trying out a slightly messy directory structure, where the codes is divided into modules that depend on each other. To get python to allow this each module needs to have a snippet in \_\_init\_\_.py that works out what the parent director is and adds it to the python path if it isn't already there. In theory this means all the modules can be accessed as if we were in the src directory, which does seem to be producing quite neat code so far.


Things to be getting on with:

  Add dot language representations to everything - Connector, Device, Junction, AbsoluteVoltage, Polarized etc
  
  Add connection seeking - Traverse all connections unless they've already been covered, keep list of nodes, edges. Spew out a list of nodes, edges in dot.
  
#  Add resistance finding. Same as above but store the chain and stop when you reach a fixed voltage. For normal voltages need to calculate voltage at other end along with the effective output impedance, then pretend to be a new src with those values.
  
#  Add voltage calculation by find above chains, getting total resistance and then doing a waited sum of all voltage sources given the resistance to them
  
  Add logic level devices that contain pins (connectables with a single connection) that do IC style things
  
  Add capacitors as a variable voltage with some ESR.
  
  Actually implement something interesting.
