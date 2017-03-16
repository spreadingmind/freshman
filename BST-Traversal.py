'''This is a task from HackerRank. traverse each level of the tree from the root downward, and 
process the nodes at each level from left to right in order to get a level-order traversal.
Sample Input

6
3
5
4
7
2
1

Sample Output

3 2 5 1 4 7 


'''
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

    def levelOrder(self, root):
        queue = []
        if root is not None:
            queue.append(root)
        while queue:
            x = queue.pop(0)
            print (x.data, end=' ')
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
        return None

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
