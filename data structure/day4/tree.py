
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val,end=' ')

def preOrder(root):
   if root:
        print(root.val,end=' ')
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val,end = ' ')
        inOrder(root.right)


def Insert(node, key):
    if(node is None):
        return Node(key)
    if(key < node.val):
        node.left = Insert(node.left, key)
    else:
        node.right = Insert(node.right, key)
    return node
        
root = None
root = Insert(root,8)
root = Insert(root,3)
root = Insert(root,1)
root = Insert(root,6)
root = Insert(root,7)
root = Insert(root,10)
root = Insert(root,14)
root = Insert(root,4)  

# root = Node(1)
# root.left = Node(2)
# root.left.left = Node(4)
# root.left.right = Node(5)

# root.right = Node(3)

print("InOrder",end=' ')
inOrder(root)
print()
print("preOrder",end=' ')
preOrder(root)
print()
print("Post order",end=' ')
postOrder(root)

