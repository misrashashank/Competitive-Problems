'''
Given the root node of a binary search tree (BST) and a value.
You need to find the node in the BST that the node's value equals
the given value. Return the subtree rooted with that node.
If such node doesn't exist, you should return NULL.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3

In the example above, if we want to search the value 5,
since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL,
therefore you would see the expected output (serialized tree format) as [],
not null.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        '''
        # Method 1: Without utilizing the fact that in a Binary Search Tree
        # all nodes left of root are less than root and
        # all nodes right of root are greater than root

        queue = [root]
        while(queue):
            curr = queue.pop(0)
            if curr.val == val:
                return curr

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return None
        '''

        # Method 2: Utilizing the properties of Binary Search Tree
        queue = [root]
        while(queue):
            curr = queue.pop(0)
            if curr.val == val:
                return curr

            if curr.val > val and curr.left:
                queue.append(curr.left)
            elif curr.val < val and curr.right:
                queue.append(curr.right)
        return None
