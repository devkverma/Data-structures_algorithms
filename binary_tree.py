class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.lchild = None
        self.rchild = None

class Solution:
    def addElement(self, tree, val):
        root = tree
        if root.val is None:
            root.val = val
            return
        if val < root.val:
            if root.lchild:
                self.addElement(root.lchild,val)
            else:
                root.lchild = TreeNode(val)
                return root
            
        elif val > root.val:
            if root.rchild:
                self.addElement(root.rchild,val)
            else:
                root.rchild = TreeNode(val)
        
        else:
            raise ValueError("Values can't be repeated")
        
    def inorder_r(self,tree):  # Inorder traversal using recursion
        root = tree
        if root == None:
            return
        self.inorder_r(root.lchild)
        print(root.val , end = ' ')
        self.inorder_r(root.rchild)
        

    def preorder_r(self,tree):  # Preorder traversal using recursion
        root = tree
        if not root:
            return
        print(root.val, end=' ')
        self.preorder_r(root.lchild)
        self.preorder_r(root.rchild)
        
    def postorder_r(self,tree):     # Postorder traversal using recursion
        root = tree
        if not root:
            return
        self.postorder_r(root.lchild)
        self.postorder_r(root.rchild)
        print(root.val , end = ' ')



sol = Solution()

t1 = TreeNode()

sol.addElement(t1,5)
sol.addElement(t1,1)
sol.addElement(t1,6)
sol.addElement(t1,10)
sol.inorder_r(t1)
print()
sol.preorder_r(t1)
print()
sol.postorder_r(t1)