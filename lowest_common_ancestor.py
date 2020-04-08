'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the
lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
of itself according to the LCA definition.

Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        # BFS
        # Initialize queue with (root, level) for BFS traversal
        queue = [root]

        # Flags to check if p and q have been discovered
        flag = 0

        # Track parent nodes
        parent_map = {root: -1}

        # Discover target node p and q
        while(flag != 2):
            # Get number of nodes on each level
            level_nodes = len(queue)

            for index in range(level_nodes):
                # Get current node
                curr_node = queue.pop(0)
                if curr_node == p or curr_node == q:
                    flag += 1

                # Add current node's children in queue
                if curr_node.left:
                    parent_map[curr_node.left] = curr_node
                    queue.append(curr_node.left)
                if curr_node.right:
                    parent_map[curr_node.right] = curr_node
                    queue.append(curr_node.right)

                if flag == 2:
                    break

        # Create ancestor set for p
        p_ancestors = {p}
        node = p
        while(True):
            if node in parent_map.keys():
                p_ancestors.add(parent_map[node])
                node = parent_map[node]
            else:
                break

        if q in p_ancestors:
            return q

        node = q
        while(True):
            if node in parent_map.keys():
                if parent_map[node] in p_ancestors:
                    return parent_map[node]
                else:
                    node = parent_map[node]
            else:
                return -1
