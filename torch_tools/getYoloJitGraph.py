import torch
import Darknet

def getgraph(cfgfile):
  m = Darknet(cfgfile)
  input = torch.randn((1, 3, 608, 608), dtype=torch.float32)
  traced = torch.jit.trace(m, input, check_trace=False)
  graph,w = torch._C._jit_pass_lower_graph(traced.graph, traced._c)
  print(graph)
