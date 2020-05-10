'''
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path 
between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by 
the number of edges between them.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.module(root)
        return self.diameter

    def module(self, node):
        if not node:
            return 0
        left = self.module(node.left)
        right = self.module(node.right)

        self.diameter = max(left + right, self.diameter)
        return max(left, right) + 1

# Solution 2
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        '''
        TreeNode > Integer
        
        Some tree > 3
        Recursive
        For each node, calculate left and right heights
        Also, recursively keep updating max_diameter at each node (left + right)
        '''
        self.max_diameter = 0
        self.get_max_diameter(root)
        return self.max_diameter
        
    def get_max_diameter(self, node):
        if not node:
            return 0

        left = self.get_max_diameter(node.left)
        right = self.get_max_diameter(node.right)

        self.max_diameter = max(self.max_diameter, left+right)

        return max(left, right) + 1
'''