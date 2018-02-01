import debug


class dotEntry(dict):
  """A simple class to represent a line of dot code. The definition must be supplied, any key-value pairs are passed on as parameters"""
  def __init__(self,definition="",*args,**kwargs):
    super(dotEntry,self).__init__(*args,**kwargs)
    self.definition = definition

  def __str__(self):
    return self.definition + " [ " + " ".join([ "\"{0}\"=\"{1}\"".format(key,value) for key,value in self.items() ]) + " ]"
  
  def __iter__(self):
    """We define an iterator that just returns this object. This way we don't need to check if we've been given a single instance or an array, we can just treat it as an array every time. Lazy, but neat."""
    return iter([self])

class Graph(list):
  def ouput(self,filename):
    with open(filename,"w") as f:
      f.writelines("\n".join(map(str,self)))
      
#@debug.alwaysDebug(debug.DebugLevels.verbose)
@debug.indented
def exploreGraph(start):

  if not hasattr(start,"__iter__"):
    start=[start]
  
  toProcess=set(start)
  processed=set()
  while True:
    if len(toProcess) == 0: break
    current=toProcess.pop()
    
    debug.verbose( "Considering ",current)
    debug.indent()
    debug.verbose( "Connects to",*current.connections )
    new=current.connections.difference(processed)
    debug.verbose( "Adding",*new )
    
    toProcess.update( new )
    debug.indent()
    debug.verbose( "Leaves",*toProcess)
    processed.add(current)
    debug.verbose( "Having done",*processed)
    debug.unindent(2)
  return processed

def graph(start):
  strings=Graph()
  strings.append("graph {")
  for entry in exploreGraph(start):
    for line in entry._dotRepr():
      strings.append(line)
  strings.append("}")
  return strings
