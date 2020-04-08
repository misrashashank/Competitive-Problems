'''
Given a non-empty, singly linked list with head node head,
return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.
(The judge's serialization of this node is [3,4,5]).

Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and
ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])

Since the list has two middle nodes with values 3 and 4,
we return the second one.

Note:
The number of nodes in the given list will be between 1 and 100.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        '''
        # Method 1: Run fast and slow pointers
        if head == None:
            return None
        # If linked list size is 1
        if head.next == None:
            return head
        # If linked list size is 2
        if head.next.next == None:
            return head.next

        back = head.next
        front = head.next.next
        while(back != None):
            if front.next == None:
                return back
            elif front.next.next == None:
                return back.next
            else:
                back = back.next
                front = front.next.next
                head = head.next
        '''
        # Method 2: Get linked list length, then traverse till middle

        # Get Linked List length
        copy_head = head
        len_ll = 0
        while(head):
            head = head.next
            len_ll += 1

        # Middle of the length
        mid = len_ll // 2

        # Traverse to the middle
        for _ in range(mid):
            copy_head = copy_head.next
        return copy_head
