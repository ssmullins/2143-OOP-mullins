"""
Programmed By: Samuel Mullins, Carlos Placencia

Program: BST - Balanced Search Tree

Description: This program takes in data in the form of integers, and puts them into a search tree.
"""

import random

"""
@Class: BalancedSearchTree
@Usage: bst = BST()

@Description: 
    This class defines what a Balanced Search Tree is made of, and declares the functions
    to be used in other classes.
        * Insert an integer.
        * Insert a list of integers.
        * Get largest and smallest integer.
        * Traverse and print the search tree.

@Params: param1 - (Int) Data - The value being passed into the search tree.

@Methods:
    insert - Gets a value from the user and passes it into the search tree, then puts it into its
             proper place in the tree.
    insertList - Gets a number from the user, and builds a list of integers the size of the number.
                 Then places the integers into a search tree in thier proper place.
    getMax - Gets the largest value stored in the search tree.
    getMin - Gets the lowest value stored in the search tree.
    traverseInOrder - Traverses the search tree and prints the values out in order.
"""
class BalancedSearchTree(object):
    def __init__(self,data):
        self.data = data
        self.root = None
        self.left = None
        self.right = None
"""
@Description: Gets a value from the user and passes it into the search tree, then puts it into its
              proper place in the tree.
@Params: Int (data).
@Returns: None
"""
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
"""
@Description: Gets a number from the user, and builds a list of integers the size of the number.
              Then places the integers into a search tree in thier proper place.
@Params: None
@Returns: Search tree filled with values from a list.
"""    
    def insertList(self):
        unique = []
        random.seed(250)
        num = int(input("Please enter a number between 1 and 100000"))
        for i in range(0,num):
            r = random.randint(0,1000000)
                
            if r not in unique:
                unique.append(r)
        
        unique.sort()
        for i in unique:
            BalancedSearchTree.insert(self, i)
"""
@Description: Gets the largest value stored in the search tree.
@Params: None
@Returns: Maximum value in the search tree.
"""    
    def getMax(self):
        if self.right is None:
            return self.data
        else:
            return self.right.getMax()
"""
@Description: Gets the lowest value stored in the search tree.
@Params: None
@Returns: Minimum value in the search tree.
"""
    def getMin(self):
        if self.left is None:
            return self.data
        else:
            return self.left.getMin()
"""
@Description: Traverses the search tree and prints the values out in order.
@Params: None
@Returns: Values in the search tree in order.
"""
    def traverseInOrder(self):
        if self.left is not None:
            self.left.traverseInOrder()
        print(self.data)
        if self.right is not None:
            self.right.traverseInOrder()
"""
@Class: BST
@Usage: bst = BST()

@Description: 
    Uses the functions declared in BinarySearchTree to build and manipulate a search tree.
        * Insert an integer.
        * Insert a list of integers.
        * Get largest and smallest integer.
        * Traverse and print the search tree.

@Params: param1 - (object) BinarySearchTree Instance of the class BinarySearchTree so we have access to its
                  data members.

@Methods:
    insert - Gets a value from the user and passes it into the search tree, then puts it into its
             proper place in the tree.
    insertList - Gets a number from the user, and builds a list of integers the size of the number.
                 Then places the integers into a search tree in thier proper place.
    getMax - Gets the largest value stored in the search tree.
    getMin - Gets the lowest value stored in the search tree.
    traverseInOrder - Traverses the search tree and prints the values out in order.
"""        
class BST(object):
    def __init__(self):
        self.rootNode = None
"""
@Description: Gets a value from the user and passes it into the search tree, then puts it into its
              proper place in the tree.
@Params: Int (data).
@Returns: None
"""
    def insert(self,data):
        if not self.rootNode:
            self.rootNode = BalancedSearchTree(data)
        else:
            self.rootNode.insert(data)#calls the method in the Node class
"""
@Description: Gets a number from the user, and builds a list of integers the size of the number.
              Then places the integers into a search tree in thier proper place.
@Params: None
@Returns: Search tree filled with values from a list.
"""    
    def insertList(self):
        self.rootNode.insertList()
"""
@Description: Gets the largest value stored in the search tree.
@Params: None
@Returns: Maximum value in the search tree.
"""        
    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax()
"""
@Description: Gets the lowest value stored in the search tree.
@Params: None
@Returns: Minimum value in the search tree.
"""
    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()
"""
@Description: Traverses the search tree and prints the values out in order.
@Params: None
@Returns: Values in the search tree in order.
"""
    def traverseInOrder(self):
        if self.rootNode:
            self.rootNode.traverseInOrder()


bst = BST()

bst.insert(50)
bst.insert(100)
bst.insert(5)
bst.insert(23)
bst.traverseInOrder()

bst.insertList()
bst.traverseInOrder()