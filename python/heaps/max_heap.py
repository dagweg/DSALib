from typing import List, Tuple
from queue import Queue
from math import floor

class Node:
  def __init__(self,value=0,left=None,right=None):
    self.value = value
    self.left = left
    self.right = right

class MaxHeap:
  def __init__(self,arr:List[int]=[]):
    if arr:
      self.heap = self.heapify(arr)
    else: 
      self.heap = [] 

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

  def _sift_down(self,arr,i):
    N = len(arr)
    while True:
      left = i * 2 + 1 
      right = i * 2 + 2

      # Out of bounds check
      if right >= N and left >= N: 
        break
      elif right >= N:
        max_i = left
      elif left  >= N:
        max_i = right
      else:
        max_i = self._get_max(left,right,arr)
      
      # print('how in the world' ,arr[i],arr[max_i])
      if arr[i] < arr[max_i]:
        arr[i], arr[max_i]  = arr[max_i] , arr[i]
      else:
        break;
      
      i = max_i

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
    N-=1

    # Perform operations to convert the modified heap back to max-heap
    i = 0

    while True:
      left = i*2 + 1
      right = i*2 + 2

      # Out of bounds check
      if right + 1 > N and left + 1 > N: break
      elif right + 1 > N:
        max_i = left
      elif left + 1 > N:
        max_i = right
      else:
        max_i = self._get_max(left,right,self.heap)

      # The element is in its right position so break
      if self.heap[i] > self.heap[max_i]: break

      # Perform a swap to bubble up the max element upward the tree
      if self.heap[i] < self.heap[max_i]:
        self.heap[i], self.heap[max_i] = self.heap[max_i], self.heap[i]

      i = max_i


  # Helper function that returns a tuple (max_element,index) | Provided that i & j are within bounds of arr
  def _get_max(self,i:int,j:int, arr) -> int:
    if arr[j] > arr[i]:
      return j
    return i

  # It converts the input array into max-heap array & return it
  def heapify(self,arr: List[int]) -> List[int]:
    if not arr: return []
    _arr = arr[:]
    N = len(_arr)
    for i in range(N-1,-1,-1):
      self._sift_down(_arr,i)
    return _arr
    
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


heap = MaxHeap([4, 10, 3, 5, 1, 10, 4])

print(heap.is_max_heap(heap.__repr__()))


# heap.insert(10)
# heap.insert(20)
# heap.insert(30)
# heap.insert(40)
# heap.insert(50)

# heap.delete()

# arr = [4, 10, 3, 5, 1, 10, 4]

# print(arr)

# print(heap.__repr__())
# print(heap.is_max_heap(arr)) # false 




