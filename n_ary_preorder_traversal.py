'''
Given an n-ary tree, return the preorder traversal of its nodes' values.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: Node) -> List[int]:
        if not root:
            return None
        tree_list = [root.val]
        for child in root.children:
            tree_list.extend(self.preorder(child))
        return tree_list
