'''
Given an n-ary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).
We should return its level order traversal:

Note:
The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
'''

"""

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        if not root: return []
        level, max_level = 0, -1
        node_q = [(level, root)]
        output_tree = []
        
        while(node_q):
            level, node = node_q.pop(0)
            if level > max_level:
                max_level = level
                output_tree.append([node.val])
            else:
                output_tree[level].append(node.val)

            for child in node.children:
                node_q.append((level+1, child))
        return output_tree
