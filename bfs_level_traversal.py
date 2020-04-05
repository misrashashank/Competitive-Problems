'''
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        else:
            tree_queue = [root]
        traversal = []
        while(tree_queue != []):
            level_traversal = []
            next_level = []
            
            for node in tree_queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                level_traversal.append(node.val)
            tree_queue = next_level
            traversal.append(level_traversal)
        return traversal
