# Table of Contents
- [Introduction](#Introduction)
- [Diagrams](#Diagrams)
- [Binary Tree Example Problem](#Binary-Tree-Example-Problem)
- [Binary Tree Problem for you to solve](#Binary-Tree-Problem-for-you-to-solve)

## What is a Binary Tree
A Binary Tree is a collections of nodes where each parent node has zero, one, or two children. A balanced binary tree with two children have the greater child on the right and the lesser child on the left. For example, a tree with a parent node of 10 would have a child of 2 on the left and a child of 11 on the right. Check out the [Diagrams](#Diagrams) for a visual. Binary trees are commonly traversed through depth first search or breadth first search.

- The Root Node is the node at the top of the tree
- The Parent Node is a node with children nodes
- The Child Node is a node with a parent
- The Leaf Node is a node without any children nodes
 ![Code example of a BinaryTree](Tree.py)

## Purpose of a Binary Tree
Binary Trees are great way to store data in a hierchy. Binary Trees are often used for sorting, data compression, and other purposes. 

## Problems that can be solved with a Binary Tree
Any problem that requires a sorted heirchy could consider using a binary tree. Binary Tree is used in Huffman code, which is a compression algorithem that creates lossless compression. Huffman code uses a binary tree with routes to different letters and symbols to save space by looking for patterns and compressing them. If you would like to learn more about Huffman code, check out this website [here](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/).
![Huffman Code(https://th.bing.com/th/id/R.b44993ee9afd517675298f5e01461662?rik=sQSObPQEiZcFzw&riu=http%3a%2f%2fi.stack.imgur.com%2f1fEJE.png&ehk=pzt1wIyP22t8MJoAS2KWuT9U55Y1TLDCRWZI%2fuRqyzk%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1))](huffmanCode.png)

## How Binary Trees are used in Python
Binary trees are created with a binary search tree parent class, and a child node class. To see an example of one, click ![here](Tree.py). Binary Trees can also be directly imported as a library using "pip install binarytree" in your terminal. This tutorial won't use this, but if you would like to use it, check out this [site](https://www.geeksforgeeks.org/binarytree-module-in-python/).

## Common errors in Binary Trees
Binary trees can be traversed in multiple ways. It can be easy to get confused and not traverse in the proper way. Learn the following methods of traversal at this [site](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/) to improve your understanding of them. 


# Diagrams

### Basic Binary Search tree
Root Node: 7

Parent-child node relationships: 
- 7 has children 3 and 12
- 3 has children of 1 and 6
- 1 has children of 0 and 2
- 6 has 4 as a child
- 4 has 5 as a child
- 12 has children 9 and 13
- 9 has children 8 and 11
- 11 has 10 as a child
- 13 has 15 as as a child
- 15 has 14 as a child

Leaf Nodes: 0,2,5,8,10,14(Nodes without Children)

![Binary Search Tree Example](Tree.jpg)

### Binary Tree Common Search methods

Breadth first search checks the nodes closest to the root node first from left to right. Depth First Search searches for values starting at the root moving down each child as deep as possible from left to right. 

![Breadth First Search and Depth First Search(https://i.imgur.com/bfitrJw.png)](tree2.png)


# Binary Tree Example Problem

Jeff needs to compare simple binary trees that his company has given him. Create a function that uses recursion to compare 2 binary trees to determine if they have the same structure and values. ![Code Solution](TreeExample.py)


# Binary Tree Problem for you to solve
Joe needs to look at two trees and see if that have matching values, but doesn't care if the trees have different structures. Create a function that checks if 2 trees have the same values(ignore duplicates, both trees are only allowed to have the same values). Don't look at the solution until you finish, but use the following code as your tree and then use the test cases when you are done.

 ```python

class TreeNode:
   def __init__(self, rootValue):
       self.currentNode = rootValue
       self.leftNode = None
       self.rightNode = None
tree1 = TreeNode(50)
tree1.leftNode = TreeNode(25)
tree1.rightNode = TreeNode(150)
tree1.rightNode.rightNode = TreeNode(275)
tree1.rightNode.rightNode.rightNode = TreeNode(300)


tree2 = TreeNode(25)
tree2.leftNode = TreeNode(50)
tree2.rightNode = TreeNode(150)
tree2.rightNode.rightNode = TreeNode(275)
tree2.rightNode.rightNode.rightNode = TreeNode(300)

tree3 = TreeNode(100)
tree3.leftNode = TreeNode(150)
tree3.rightNode = TreeNode(50)
tree3.rightNode.rightNode = TreeNode(200)
tree3.rightNode.rightNode = TreeNode(250)

## Do not edit code above, start coding here

def checkEqualTreeValues(treeNumber1,treeNumber2,list1 = [],list2 = []):
  pass

## Test cases below, do not edit
print(checkEqualTreeValues(tree1,tree2)) # Should return true, same tree order and values
print(checkEqualTreeValues(tree2,tree3)) # Should return false, same tree values but different order
```
![Code Solution](TreeProblem.py)