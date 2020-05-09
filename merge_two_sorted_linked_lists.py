'''
Merge two sorted linked lists and return it as a new list. The new list
should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return -1

        # First, create a new ListNode object with any value
        # new_head refers to the first node (with value 100)
        # l3 points to this node
        new_head = ListNode(100)
        l3 = new_head

        # Merge sorted nodes
        while(l1 and l2):
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        if l1:
            l3.next = l1
        else:
            l3.next = l2

        # Return the node from the point where the merged nodes start
        # We can't use l3, as l3 is at present at the end of the sorted list
        return new_head.next


# Another solution
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        LL1, LL2 > LL4
        Sorted linked lists
        
        1->2->4, 1->3->4 > 1->1->2->3->4->4
        1->2->4, 1 > 1->1->2->4
        1, 1 > 1->1
        1,  > 1
         , > None
        
        Two pointers on each LL > Compare value > Create new ListNode
        Maintain condition that either of the lists is present
        
        Return dummynode->1->1->2
        
        Time: O(n)
        Space: O(1)
        '''
        
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return None
        
        root = ListNode(0)
        head = root
        
        while(l1 and l2):
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next
            head = head.next
        if l1:
            remainder = l1
        else:
            remainder = l2
        while(remainder):
            head.next = ListNode(remainder.val)
            remainder = remainder.next
            head = head.next
        return root.next
'''
