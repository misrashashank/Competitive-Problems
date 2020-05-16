'''
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # Method 1: Iterative approach
        '''
        ListNode > ListNode
        
        1->2->3->4->5->NULL => 5->4->3->2->1->NULL
        
        1>2>3>4
        1<2<3>4

        prev = None
        curr = prev
        prev = curr
        '''
        '''
        curr = head
        prev = None
        
        while(curr is not None):
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        return prev
        '''

        # Method 2: Recursive approach
        '''
        Base condition
        curr_
        
        Sub-problem
        
        '''
        if (head is None) or (head.next is None):
            return head
        
        node = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        return node
