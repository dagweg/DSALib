from typing import List,Dict
from queue import Queue

class Node:
  def __init__(self,v:int,u:int=-1,w:int=-1):
    self.v = v
    self.u = u
    self.w = w

class UndirectedGraph:

  def __init__(self,vertices,weighted=False):
    pass

  def add_vertex(self,v:int):
    pass

  def remove_vertex(self,v:int):
    pass

  def add_edge(self,v:int,u:int):
    pass

  def remove_edge(self,v:int,u:int):
    pass

  def find(self,v:int) -> int:
    pass
  
  def find(self,v:int,u:int) -> List[int]:
    pass

  def has_edge(self,v:int,u:int) -> bool:
    pass

  def dfs(self) -> List[int]:
    pass

  def bfs(self) -> List[int]:
    pass
    


