import Connectable

import Junction

import Infrastructure.debug as debug


class Device(Connectable.Connectable):
  """ A device is a more complex object, like a voltage supply or an IC. The only point of this class at present is to have it drawn as a cluster in dot, so it has a pretty box around it. Which I haven't started implementing. Yay!"""
  pass

  def _dotRepr(self):
    raise NotImplementedError("Need to think how to ensure the right bits are contained within the subgraph")
    return "subgraph cluster_"+self._dotName()+" {}"
