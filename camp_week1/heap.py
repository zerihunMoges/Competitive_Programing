class Solution:
    
    #Heapify function to maintain heap property.
    def up(self, arr,n,i ):
        while i > 0 and arr[self.parent(i)] > arr[i]:
            
            arr[self.parent(i)], arr[i] = arr[i], arr[self.parent(i)]
            i = self.parent(i)
        return arr


    def down(self, arr, n , i):
        
        if self.leftChild(i) < n:
            minchild = self.leftChild(i)
       
            if self.rightChild(i) < n:
                if arr[minchild] > arr[self.rightChild(i)]:
                    minchild = self.rightChild(i)
            if arr[minchild] < arr[i]:
                arr[minchild], arr[i] = arr[i], arr[minchild]
                self.down(arr, n, minchild)
        return arr 
              
    def heapify(self,arr, n, i):
        
        self.up(arr, n, i)
        self.down(arr,n,i)
        
            
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        arr.sort()
        
    def insert(self, element, arr):
      
        arr.append(element)
        n = len(arr)
        arr = self.heapify(arr, n, n-1)
        return arr
        
    def remove(self, i, arr):
        arr[len(arr)-1], arr[i] = arr[i], arr[len(arr)-1]
        arr.pop(-1)
        n = len(arr)
        
        if i != n:
            arr = self.heapify(arr, len(arr), i)
            return arr
            
        return arr
        
    def update(self, i, arr):
        arr[len(arr)-1], arr[i] = arr[i], arr[len(arr)-1]
        arr.pop(-1)
        self.heapify(arr, len(arr), i-1)
        
    def getMin(self, arr):
        return arr[0]
            
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        
        for i in range(len(arr)-1, -1, -1):
            self.heapify(arr, len(arr), i)
       
        
        
        for i in range(len(arr)-1, -1, -1):
            arr[i], arr[0] = arr[0],arr[i]
            self.down(arr, i, 0)
        

        arr.reverse()
        return arr
            
        
        
    def leftChild(self, i):
        return 2*i + 1 
    def rightChild(self, i):
        return 2*i + 2
    def parent(self, i):
        return (i-1)//2 if (i-1) > -1 else 0
