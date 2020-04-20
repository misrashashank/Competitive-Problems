'''
Given the root node of a binary search tree (BST) and a value to be inserted
into the tree, insert the value into the BST.
Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion,
as long as the tree remains a BST after insertion. You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5

You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5

This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        '''
        BST, val > Insert in BST > Maintain a BST
        root node, val > root
        root node is null > return val node as root
        BST > root greater than left, root less than right
        Traversing from root > Check if root value is less or greater than input val
        If less, go left, else, go right
        Find a node which doesn't have a child node in the direction we're heading
        (input value satisfies the constraint) > Then insert
        '''

        '''
        Method 1: Iteration

        # if not root:
        #     return TreeNode(val)

        curr_node = root
        while(curr_node):
            # Compare node value with input val
            if curr_node.val > val:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = TreeNode(val)
                    return root

            else:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = TreeNode(val)
                    return root
        return TreeNode(val)
        '''

        # Method 2: Recursion
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root
