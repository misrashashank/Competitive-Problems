'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

Example:
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        def check_inorder(left_i, right_i):

            # Base case
            if left_i > right_i:
                return None

            # Get the first element in preorder
            root_val = preorder.pop(0)

            # Create a TreeNode for the first element
            root = TreeNode(root_val)

            # Get the index of first element from preorder in inorder traversal
            root_i = inorder.index(root_val)

            # Break inorder as per the root node
            # As per the preorder traversal, first create left subtree,
            # then right subtree
            root.left = check_inorder(left_i, root_i - 1)
            root.right = check_inorder(root_i + 1, right_i)

            return root

        root = check_inorder(0, len(inorder)-1)
        return root
