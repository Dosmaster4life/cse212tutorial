
class TreeNode:
   def __init__(self, rootValue):
       self.currentNode = rootValue
       self.leftNode = None
       self.rightNode = None

tree1 = TreeNode(100)
tree1.leftNode = TreeNode(50)
tree1.rightNode = TreeNode(150)
tree1.rightNode.rightNode = TreeNode(200)


tree2 = TreeNode(100)
tree2.leftNode = TreeNode(50)
tree2.rightNode = TreeNode(150)
tree2.rightNode.rightNode = TreeNode(200)

tree3 = TreeNode(100)
tree3.leftNode = TreeNode(150)
tree3.rightNode = TreeNode(50)
tree3.rightNode.rightNode = TreeNode(200)


tree4 = TreeNode(0)

tree5 = TreeNode(0)

## Do not edit any code above this line


def compareTrees(treeNumber1,treeNumber2):
   if treeNumber1 is None or treeNumber2 is None : 
      return treeNumber1 is treeNumber2
   else: # use recursion to check if current nodes match and left/right nodes match
      return treeNumber1.currentNode == treeNumber2.currentNode and compareTrees(treeNumber1.leftNode,treeNumber2.leftNode) and compareTrees(treeNumber1.rightNode,treeNumber2.rightNode)


## Test cases below, do not edit
print(compareTrees(tree1,tree2)) # Should return true, same tree order and values
print(compareTrees(tree2,tree3)) # Should return false, same tree values but different order
print(compareTrees(tree4,tree5)) # Empty Trees other than 1 node with a value of 0 should return true