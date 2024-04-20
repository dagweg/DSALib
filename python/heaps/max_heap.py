from typing import List
from math import floor

class Node:
  def __init__(self,value=0,left=None,right=None):
    self.value = value
    self.left = left
    self.right = right

class MaxHeap:
  def __init__(self):
    self.heap = []

  def insert(self,value: int):
    self.heap.append(value)
    N = len(self.heap)
    i,p = N-1, N-1
    
    while i != 0:
      p = (i-1) // 2
      if self.heap[p] < self.heap[i]:
        self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
      i = p
    
    print(self.heap)

  def delete(self):
    pass

  def heapify(self, arr: List):
    pass

  def get_array(self):
    pass


heap = MaxHeap()

heap.insert(0)
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(9)
heap.insert(11)
