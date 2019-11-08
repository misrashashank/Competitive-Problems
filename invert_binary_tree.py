'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: 
            return root
        node_stack = [root]
        
        while(node_stack):
            curr_node = node_stack.pop()
            
            if curr_node.left or curr_node.right:
                temp = curr_node.left
                curr_node.left = curr_node.right
                curr_node.right = temp
            
            if curr_node.left:
                node_stack.append(curr_node.left)
            if curr_node.right:
                node_stack.append(curr_node.right)
        return root
