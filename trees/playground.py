
"""

1. Create a root node.
2.


"""




class node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        pass


    def addRecursive(self, current, data):

        if current == None:
            return Node(data)

        if (data < current.data):
            current.left = addRecursive(current.left, data)

        elif (data > current.data):
           current.right = addRecursive(current.right )






