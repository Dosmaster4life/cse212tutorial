class binarySearchTree:
    class Node:

        def __init__(self, data):
           
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = binarySearchTree.Node(data)
        else:
            self._insert(data, self.root)  

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = binarySearchTree.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:

            if node.right is None:
                node.right = binarySearchTree.Node(data)
            else:

                self._insert(data, node.right)
    


    def __contains__(self, data):
        return self._contains(data, self.root) 


    def _contains(self, data, node):
        if node is None:
           return False
        else:
            if data == node.data:
                return True
            if data < node.data:
                return self._contains(data,node.left)
            elif data > node.data:
                return self._contains(data,node.right)
        return False
            

    def __iter__(self):
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
      
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):

        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):

        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root) 

    def _get_height(self, node):
      
        if node is None:
            return 0  
        else:
            return max(self._get_height(node.left),self._get_height(node.right)) + 1


def _insert_middle(sorted_list, first, last, binarySearchTree):

    if sorted_list :
        middleOfList = (first + last)//2
        binarySearchTree.insert(sorted_list[middleOfList])
        firstList = sorted_list[:middleOfList]
        secondList = sorted_list[1+ middleOfList:]

        _insert_middle(firstList, 0, len(firstList)-1, binarySearchTree)
        _insert_middle(secondList, 0, len(secondList)-1, binarySearchTree)
    return

