# LogicSim
A very basic attempt at a voltage driven logic IC simulation.

So far all that's been decided is that there are three main types of 'thing', connectors, that go between two points, junctions where connectors meet, and 'other', where other things happen (voltages are set and measured, for example)

I'm trying out a slightly messy directory structure, where the codes is divided into modules that depend on each other. To get python to allow this each module needs to have a snippet in \_\_init\_\_.py that works out what the parent director is and adds it to the python path if it isn't already there. In theory this means all the modules can be accessed as if we were in the src directory, which does seem to be producing quite neat code so far.
