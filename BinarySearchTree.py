class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root == None: #empty tree
            height = -1
        elif root.left == None and root.right == None: #leaf
            height = 0
        else:
            leftHeight = self.getHeight(root.left)
            rightHeight = self.getHeight(root.right)
            height = 1 + max(leftHeight, rightHeight)

        return height


T = int(input())
myTree = Solution()
root = None
for i in range(T):
 data = int(input())
 root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)