'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         node_stack = [(1, root)]
#         max_level = 1
        
#         while(node_stack):
#             level, node = node_stack.pop()
#             if level > max_level:
#                 max_level = level
            
#             if node.left:
#                 node_stack.append((level+1, node.left))
#             if node.right:
#                 node_stack.append((level+1, node.right))
#         return max_level

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left) + 1
            right = self.maxDepth(root.right) + 1
            return max(left, right)
