class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    
    def __str__(self):
        return str(self.val)
    
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(6)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F 

def preorder(node):
    if not node:
        return 
    print(node)
    preorder(node.left)
    preorder(node.right)

print(preorder(A))
     # root=>left=>right


def inorder(node):
    if not node:
        return 
    inorder(node.left)
    print(node)
    inorder(node.right)
print(inorder(A))
# left=>root=>right


def postorder(node):
    if not node:
        return 
    postorder(node.left)
    postorder(node.right)
    print(node)
print(postorder(A))
# left=>right=>root