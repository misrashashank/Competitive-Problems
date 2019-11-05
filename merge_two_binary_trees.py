'''
Given two binary trees and imagine that when you put one of them 
to cover the other, some nodes of the two trees are overlapped 
while the others are not.

You need to merge them into a new binary tree. 
The merge rule is that if two nodes overlap, then sum node values up 
as the new value of the merged node. Otherwise, the NOT null node 
will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 
Note: The merging process must start from the root nodes of both trees.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        left1, right1, left2, right2 = None, None, None, None
        inter_sum = 0
        
        # Initialize output tree
        t3 = TreeNode(0)
        
        # Check if at least one of the 2 nodes are present
        if t1 or t2:
            if t1:
                inter_sum += t1.val
                left1 = t1.left
                right1 = t1.right
            if t2:
                inter_sum += t2.val
                left2 = t2.left
                right2 = t2.right
            t3.val = inter_sum
            
            t3.left = self.mergeTrees(left1, left2)
            t3.right = self.mergeTrees(right1, right2)
            
            return t3
        else:
            return None

        return t3
