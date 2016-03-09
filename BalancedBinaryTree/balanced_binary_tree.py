import random 
 
class BalancedSearchTree(object): 
    def __init__(self,size = input("Number to insert: (1-100000) ")): 
        self.tree = [-1 for x in range(size)] 
        self.size = size 
        self.root = 1 
        self.items = 0 
    print (self.size)
      
    def insert(self,val): 
         # If list (tree) is empty, put value at root 
        if self.tree[self.root] == -1: 
            self.tree[self.root] = val 
         # loop until you find the location to insert 
         # even if you have to extend this list 
        else: 
            i = self.root 
            loop = True 
            while loop: 
                if val > self.tree[i]: 
                    i = self.rightChild(i) 
                else: 
                    i = self.leftChild(i) 
                  
                if i >= self.size: 
                    self.extend() 
                  
                if self.tree[i] == -1: 
                    self.tree[i] = val 
                    self.items += 1 
                    loop = False 
              
          
    def extend(self): 
        temp = [-1 for x in range(self.size)] 
        self.tree.extend(temp) 
        self.size *= 2 
        print(self.items) 
          
    def find(self,key): 
      
        self.comparisons = 1 
 
 
        if key == self.tree[self.root]: 
            return True 
        else: 
            i = self.root 
            while True: 
                if key < self.tree[i]: 
                    i = self.leftChild(i) 
                else: 
                    i = self.rightChild(i) 
                      
                if i >= self.size: 
                    return False 
                  
                if self.tree[i] == -1: 
                    return False    
                      
                if self.tree[i] == key: 
                    return True 
                      
                self.comparisons += 1 
                  
                  
    def leftChild(self,i): 
        return 2 * i 
          
    def rightChild(self,i): 
        return 2 * i + 1 
          
# random.seed(342345) 
# bs = BinarySearchTree(4096) 
# for x in range(1000): 
#     bs.insert(random.randint(0,99999)) 