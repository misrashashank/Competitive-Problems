'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

Example:
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder, postorder):

        def check_inorder(left_idx, right_idx):
            if left_idx > right_idx:
                return None

            # Current root node will be the last element of postorder
            root_node = postorder.pop()

            # Create a TreeNode from the root_node
            tree = TreeNode(root_node)

            # Get the index of the root_node in inorder traversal
            root_node_index = inorder.index(root_node)

            # Create left and right subtrees
            tree.right = check_inorder(root_node_index+1, right_idx)
            tree.left = check_inorder(left_idx, root_node_index-1)
            return tree

        root = check_inorder(0, len(inorder)-1)
        return root
