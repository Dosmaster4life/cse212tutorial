
class TreeNode:
    def __init__(self, rootValue):
       self.currentNode = rootValue
       self.leftNode = None
       self.rightNode = None
       
tree1 = TreeNode(25)
tree1.leftNode = TreeNode(50)
tree1.rightNode = TreeNode(150)
tree1.rightNode.rightNode = TreeNode(275)
tree1.rightNode.rightNode.rightNode = TreeNode(300)


tree2 = TreeNode(50)
tree2.leftNode = TreeNode(25)
tree2.rightNode = TreeNode(150)
tree2.rightNode.rightNode = TreeNode(275)
tree2.rightNode.rightNode.rightNode = TreeNode(300)

tree3 = TreeNode(100)
tree3.leftNode = TreeNode(150)
tree3.rightNode = TreeNode(50)
tree3.rightNode.rightNode = TreeNode(200)
tree3.rightNode.rightNode = TreeNode(250)


## Do not edit any code above this line


def checkEqualTreeValues(treeNumber1,treeNumber2,list1 = [],list2 = []):
  
  if(treeNumber1 is not None and treeNumber1.currentNode is not None):
    list1.append(treeNumber1.currentNode)
  if(treeNumber2 is not None and treeNumber2.currentNode is not None):
    list2.append(treeNumber2.currentNode)
  if(treeNumber1 is not None and treeNumber1.leftNode is not None):
     checkEqualTreeValues(treeNumber1.leftNode,treeNumber2.leftNode,list1,list2)
  if(treeNumber1 is not None and treeNumber1.rightNode is not None): 
    checkEqualTreeValues(treeNumber1.rightNode,treeNumber2.rightNode,list1,list2)
  if(treeNumber2 is not None and  treeNumber2.leftNode is not None): 
    checkEqualTreeValues(treeNumber1.leftNode,treeNumber2.leftNode,list1,list2)
  if(treeNumber2 is not None and treeNumber2.rightNode is not None): 
    checkEqualTreeValues(treeNumber1.rightNode,treeNumber2.rightNode,list1,list2)
  
  return set(list2) == set(list1) # remove duplicates and return
    



## Test cases below, do not edit
print(checkEqualTreeValues(tree1,tree2)) # Should return true, same tree order and values
print(checkEqualTreeValues(tree2,tree3)) # Should return false, same tree values but different order
