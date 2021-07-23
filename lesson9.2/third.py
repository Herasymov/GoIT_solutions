# class Node of binary tree
class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.left = l
        self.right = r


def insertToNode(root, val):
    if not root: return Node(val)
    elif root.val <= val:
        root.right = insertToNode(root.right, val)
    else:
        root.left = insertToNode(root.left, val)
    return root

values = [8, 3, 6, 10, 1, 14, 13, 4, 7]
root = None
for i in values:
    root =insertToNode(root, i)

print(root.val)
print(root.left.val, end=" ")
print(root.right.val)
print(root.left.left.val, end=" ")
print(root.left.right.val, end=" ")
print(root.right.right.val)