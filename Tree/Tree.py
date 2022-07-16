class BinarySearchTree:
    class Node:
        def __init__(self, data):
           
            self.data = data
            self.left = None
            self.right = None
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BinarySearchTree.Node(data)
        else:
            self._insert(data, self.root)  

    def _insert(self, data, node): # Insert data into binary tree, uses recursion to find where to insert data.
        if data < node.data:
            if node.left is None:
                node.left = BinarySearchTree.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:

            if node.right is None:
                node.right = BinarySearchTree.Node(data)
            else:

                self._insert(data, node.right)


    def contains(self, data, node): # Finds if data is in Binary Tree
        if node is None:
           return False
        else:
            if data == node.data:
                return True
            if data < node.data:
                return self.contains(data,node.left)
            elif data > node.data:
                return self.contains(data,node.right)
        return False

    def __iter__(self): # Traverses forward through in order traversal
        yield from self._traverse_forward(self.root)  
        
    def _traverse_forward(self, node):  # Traverses forward through in order traversal(left to right)
      
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self): # Traverses reversed
        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):

        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self): # gets the height of the binary tree
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root) 


   
    def _get_height(self, node):
      
        if node is None:
            return 0  
        else:
            return max(self._get_height(node.left),self._get_height(node.right)) + 1
