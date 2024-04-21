from typing import List, Tuple
from queue import Queue
from math import floor

class Node:
  def __init__(self,value=0,left=None,right=None):
    self.value = value
    self.left = left
    self.right = right

class MaxHeap:
  def __init__(self):
    self.heap = [] # store the heap values
    self.heapd = [] # store the deleted heap values

  def insert(self,value: int):
    self.heap.append(value)
    self._sift_up()

  def _sift_up(self):
    N = len(self.heap)
    i,p = N-1, N-1
    
    while i != 0:
      p = (i-1) // 2
      if self.heap[p] < self.heap[i]:
        self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
      i = p

  def delete(self):
    N = len(self.heap)
    
    # Handle Case Empty
    if N == 0: return
      
    # Add the deleted first elem to heapd
    self.heapd.append(self.heap[0]) 

    # Bring the last elem to first
    self.heap[0] = self.heap[-1]

    # Splice the heap upto last index
    self.heap = self.heap[:-1]

    # Perform operations to convert the modified heap back to max-heap
    i = 0

    while True:
      left = i*2 + 1
      right = i*2 + 2

      # Out of bounds check
      if right + 1 > N: break

      max_elem, max_i = self._get_max(self.heap,left,right) 

      # The element is in its right position so break
      if self.heap[i] > max_elem: break

      # Perform a swap to bubble up the max element upward the tree
      if self.heap[i] < max_elem:
        self.heap[i], self.heap[max_i] = self.heap[max_i], self.heap[i]

      i = max_i


  # Helper function that returns a tuple (max_element,index) | Provided that i & j are within bounds of arr
  def _get_max(self,arr: List,i: int,j: int) -> Tuple[int,int]:
    if arr[j] > arr[i]:
      return (arr[j],j)
    return (arr[i],i)

  # It converts the input array into max-heap array & return it
  def heapify(arr: List[int]) -> List[int]:
    pass    

  # Checks if input array is max-heap or not
  def is_max_heap(self,arr: List[int]) -> bool:
    i = 0
    N = len(arr)
    q = Queue()
    q.put(0)
    while not q.empty():
      i  = q.get()
      left = i * 2 + 1
      right = i * 2 + 2

      if 0 <= left < N:
        if arr[i] < arr[left]: return False
        q.put(left)
      if 0 <= right < N:
        if arr[i] < arr[right]: return False
        q.put(right)

    return True


  def get_array(self):
    pass


  def __repr__(self):
    return self.heap


heap = MaxHeap()

heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(40)
heap.insert(50)

# heap.delete()


print(heap.is_max_heap([5,4,3,2,1]))


