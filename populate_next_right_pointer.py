'''
You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children. The binary tree has the below definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count
as extra space for this problem.
'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # BFS
        # Initialize queue with root node for BFS
        q = [root]

        # Traverse using BFS
        while(q):
            # Get number of nodes at each level
            level_size = len(q)
            for index in range(level_size):
                # Get current node
                curr_node = q.pop(0)

                # Create pointer for current node to next right node
                # for all nodes except the last node for the level
                if index != level_size - 1:
                    curr_node.next = q[0]

                # Add current node's children in queue
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
        return root
