'''
Given a complete binary tree, count the number of nodes.

Note:
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are
as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example:
Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Method 1: Naive solution - BFS


class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        queue = [root]
        count = 0
        while(queue):
            curr = queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            count += 1
        return count


# Method 2: Use binary search and find nodes in only last level
# To be implemented
