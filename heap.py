class MinHeap :

  def __init__(self, maxsize) -> None:
    self.maxsize = maxsize
    self.size = 1
    self.Heap = [1]*(maxsize + 1)


  def parent(self,index):
    return index//2
  
  def left(self,index):
    return index*2
  
  def right(self,index):
    return (index * 2) + 1
  
  def isLeaf(self, index):
    return (index*2) > self.size
  
  def swap(self, uppernode, lowernode):
    self.Heap[uppernode], self.Heap[lowernode] = self.Heap[lowernode], self.Heap[uppernode]

  def minHeapify(self,index):

    if (self.Heap[index] > self.Heap[self.left(index)]) or (self.Heap[index] > self.Heap[self.right(index)]):

      if self.Heap[self.leftChild(index)] < self.Heap[self.rightChild(index)]: 
                    self.swap(index, self.leftChild(index)) 
                    self.minHeapify(self.leftChild(index)) 
      
      else: 
                    self.swap(index, self.rightChild(index)) 
                    self.minHeapify(self.rightChild(index)) 


  def insert(self, element):
      
      if self.size >= self.maxsize:
          return
      self.size += 1
      self.Heap[self.size] = element

      current = self.size

      while self.Heap[current] < self.Heap[self.parent(current)]:
          self.swap(current, self.parent(current))

  

  def printHeap(self):
      for  i in range(1, (self.size//2) + 1):
               print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
               

  def remove(self):
      
      popped = self.Heap[1]
      self.Heap[1] = self.Heap[self.size]
      self.size -=1

      self.minHeapify(0)
      return popped
  



if __name__ == "__main__": 
      
    print('The minHeap is ') 
    minHeap = MinHeap(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(11) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
 
  
    minHeap.printHeap() 
    print("The Min val is " + str(minHeap.remove())) 
  

  

