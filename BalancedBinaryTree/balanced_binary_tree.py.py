"""
Programmed By: Samuel Mullins, Carlos Placencia
"""

import random

class BalancedSearchTree(object):
    def __init__(self,data):
        self.data = data
        self.root = None
        self.left = None
        self.right = None


    def insert(self,data):
        if data < self.data:
            if not self.left:
                self.left = BalancedSearchTree(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = BalancedSearchTree(data)
            else:
                self.right.insert(data)

    def getMax(self):
        if self.right is None:
            return self.data
        else:
            return self.right.getMax()

    def getMin(self):
        if self.left is None:
            return self.data
        else:
            return self.left.getMin()

    def traverseInOrder(self):
        if self.left is not None:
            self.left.traverseInOrder()
        print(self.data)
        if self.right is not None:
            self.right.traverseInOrder()
        
class BST(object):
    def __init__(self):
        self.rootNode = None

    def insert(self,data):
        if not self.rootNode:
            self.rootNode = BalancedSearchTree(data)
        else:
            self.rootNode.insert(data)#calls the method in the Node class

    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax()

    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()

    def traverseInOrder(self):
        if self.rootNode:
            self.rootNode.traverseInOrder()

L = []
random.seed(250)
num = int(input("Please enter a number between 1 and 100000"))
for i in range(0,num):
    L.append(random.randrange(1,100000,1))
print(L)

bst = BST()
for i in L:
    bst.insert(i)
bst.traverseInOrder()
        
    
