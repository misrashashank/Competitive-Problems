'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
1. The left subtree of a node contains only nodes with keys
less than the node's key.
2. The right subtree of a node contains only nodes with keys
greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        TreeNode > Boolean
        
        [2,1,3] > True
        [] > False
        
        Traverse BFS/DFS > Check each node
        left child value < value < right child value (if child exists)
        
        Time: O(V+E)
        Space: O(V)
        '''
        
        # This approach won't work because this checks
        # the immediate children only
        # We need to check all the nodes in the left and right subtree
        '''
        if not root:
            return True
        
        bfs_queue = [root]
        while(bfs_queue):
            curr_node = bfs_queue.pop(0)
            if curr_node.left:
                if curr_node.left.val >= curr_node.val:
                    return False
                bfs_queue.append(curr_node.left)
            
            if curr_node.right:
                if curr_node.right.val <= curr_node.val:
                    return False
                bfs_queue.append(curr_node.right)
        return True
        '''
        
        # Using inorder traversal
        # Time: O(n), Space: O(n)
        '''
        Get inorder traversal > It should be strictly increasing
        '''
        if not root:
            return True
        
        inorder = []
        last_val = float('-inf')

        def inorder_traversal(node):
            if node.left:
                inorder_traversal(node.left)
            inorder.append(node.val)
            if node.right:
                inorder_traversal(node.right)
            return inorder
        
        inorder = inorder_traversal(root)
        
        for item in inorder:
            if item <= last_val:
                return False
            last_val = item
        return True
