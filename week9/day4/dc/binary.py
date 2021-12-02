class Node:

    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def add_node(self, root, node):
        
        if root is None:
            return node

        if root.value < node.value:
            #go right
            root.right = self.add_node(root.right, node)
        else:
            #go left
            root.left = self.add_node(root.left, node)


    def search(self, root, value):
        
        if root.value == value:
            return root

        if root.value > value:
            #go left
           return self.search(root.left, value)    
        else:
            #go right
            return self.search(root.right, value)
        
root = Node(None, None, 8)
node3 = Node(None, None, 3)
node10 = Node(None, None, 10)

root.add_node(root, node3)
root.add_node(root, node10)

root.search(root, 3)