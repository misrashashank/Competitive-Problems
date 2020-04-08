'''
Given a binary tree

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

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]

Explanation: Given the above binary tree (Figure A), your function
should populate each next pointer to point to its next right node,
just like in Figure B. 
The serialized output is in level order as connected by the next pointers,
with '#' signifying the end of each level.

Constraints:
The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100 
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
        # Initialize queue with root node for BFS traversal
        q = [root]

        while(q):
            # Get number of nodes for each level
            level_nodes = len(q)
            for index in range(level_nodes):
                # Get current node from the level
                curr_node = q.pop(0)

                # Add current node's children to the queue
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)

                # Create pointer for each node
                # If not last node on the level
                if index != level_nodes - 1:
                    curr_node.next = q[0]

                # if last node on the level
                else:
                    curr_node.next = None

        return root
