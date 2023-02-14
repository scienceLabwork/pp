# LAB PP Q10 A
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insert(self, root, x):
        if(root):
            if(root.val > x):
                if(root.left):
                    self.insert(root.left, x)
                else:
                    root.left = TreeNode(x)
            else:
                if(root.right):
                    self.insert(root.right, x)
                else:
                    root.right = TreeNode(x)
        else:
            root = TreeNode(x)

    def inorder(self, root):
        if(root):
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)
    
    def preorder(self, root):
        if(root):
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self, root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=" ")

    def search(self, root, x):
        if(root):
            if(root.val == x):
                return True
            elif(root.val > x):
                return self.search(root.left, x)
            else:
                return self.search(root.right, x)
        else:
            return False

x = [1,8,11,19,3,7,21]
root = TreeNode(x[0])
x = x[1:]
for i in range(len(x)):
    Solution().insert(root, x[i])

print("In order")
Solution().inorder(root)
print("\nPre order")
Solution().preorder(root)
print("\nPost order")
Solution().postorder(root)
print("\nSearch")
print(Solution().search(root, 9))