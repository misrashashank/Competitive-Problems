'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain
a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        '''
        LL1, LL2 > LL
        (2 -> 4 -> 3) + (5 -> 6 -> 4) > 7 -> 0 -> 8
        (2 -> 4 -> 3) + (0) > (2 -> 4 -> 3)
        (0) + (0) > 0
        (0) + (0 -> 0 -> 0) > 0
        
        Iterate > Sum and track carry > Create node at every step
        '''
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return ListNode(0)
        
        root = ListNode(0)
        head = root
        
        carry = 0
        while(l1 or l2):
            new_sum = carry
            carry = 0
            if l1:
                new_sum += l1.val
            if l2:
                new_sum += l2.val
            print("before: ", new_sum)
            if new_sum > 9:
                carry = 1
                new_sum -= 10
            print(new_sum)
            head.next = ListNode(new_sum)
            head = head.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry == 1:
            head.next = ListNode(1)
        return root.next
