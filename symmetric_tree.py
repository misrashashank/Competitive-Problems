'''
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Solution
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        def check_children(l_node, r_node):
            if not l_node and not r_node:
                return True
            if l_node and r_node and l_node.val == r_node.val:
                if check_children(l_node.left, r_node.right) and check_children(l_node.right, r_node.left):
                    return True
            return False

        return check_children(root.left, root.right)
