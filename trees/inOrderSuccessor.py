

tree = [2,1,3]

p = 2
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Node:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def inOrderSuccessor(root, p):
    """

    :param root: root of the tree or subtree
    :param p: node of which, successor is to be found out
    :return:
    """
    ans = None

    root = 
    while root != None:
        if root.val > p.val:
            ans = root
            # move to the left subtree to find the closest successor
            root = root.left
        else:
            # move to the right subtree to find the closest successor, if current node's value is less than or equal to p.
            root = root.right
    return ans

ans = inOrderSuccessor(tree, p)
print(ans)