from typing import List,Dict
from queue import Queue

class Node:
  def __init__(self,v,w):
    self.v = v
    self.w = w

class UndirectedGraph:

  def __init__(self,vertices=[],weighted=False):
    self.vertices = vertices
    self.edge_list = {
      v: [] for v in vertices
    }

  def add_vertex(self,v):
    if v in self.edge_list: 
      raise Exception('Vertex is already present inside the graph')
    
    self.edge_list[v] = []

  def remove_vertex(self,v):
    if not v in self.edge_list: 
      raise Exception('Vertex doesnt exist inside the graph')
    
    for u,w in self.edge_list[v]:
      for i,elem in enumerate(self.edge_list[u]):
        if elem[0] == v: self.edge_list[u].pop(i)     
    
    self.edge_list.pop(v)

  def get_edge_list(self):
    return self.edge_list

  def add_edge(self,v,u):
    if not self.find(v):
      raise Exception(f'{v} doesnt exist in the edge list')
    if not self.find(u):
      raise Exception(f'{u} doesnt exist in the edge list')
    
    if not self.has_edge(v,u):
      self.edge_list[v] += [u,0]
      self.edge_list[u] += [v,0]
    


  def remove_edge(self,v,u):
    pass

  def find(self,v):
    return v in self.edge_list
  
  def find(self,v,u):
    pass

  def has_edge(self,v,u) -> bool:
    if not self.find(v):
      raise Exception(f'{v} doesnt exist in the edge list')
    if not self.find(u):
      raise Exception(f'{u} doesnt exist in the edge list')
    
    for _u,w in self.edge_list[v]:
      if _u == u: return True
    return False

  def dfs(self) -> List[int]:
    pass

  def bfs(self) -> List[int]:
    pass
    


ug = UndirectedGraph([1,2,3])

print(ug.get_edge_list())

ug.add_vertex(10)
ug.add_vertex(11)

print(ug.get_edge_list())

ug.remove_vertex(10)

print(ug.get_edge_list())

ug.add_edge(10,11)
print(ug.get_edge_list())