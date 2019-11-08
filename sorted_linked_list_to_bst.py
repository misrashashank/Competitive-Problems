'''
Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a 
binary tree in which the depth of the two subtrees of every node 
never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents 
the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None

        # Create array out of linked list
        node_list = [head.val]
        while(head.next):
            node_list.append(head.next.val)
            head = head.next
        root = self.create_bst(node_list)
        return root

    def create_bst(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.create_bst(nums[:mid])
        node.right = self.create_bst(nums[mid+1:])
        return node
