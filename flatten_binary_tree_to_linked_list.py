# 114. Flatten Binary Tree to Linked List
# #recursive #preorder #binary tree

# go to most right node (w/ recursive) and go up 
# adding the prev node on the right side of the current root
# 6                 ->   5                  ->   4                  ->   3   ->   2   ->    1
# add nth to right      add 6 to the right      add 5 to the right ...


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    temp = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root:
            if root.right:
                print("r", root.right.val)
                self.flatten(root.right)

            if root.left:
                print("l", root.left.val)
                self.flatten(root.left)
            print("next step", root.val)
            root.right = self.temp
            root.left = None
            print("root", root.val)
            self.temp = root