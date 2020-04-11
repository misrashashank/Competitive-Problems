'''
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        # Method 1: Create array from linked list, then compare
        # Time: O(n)
        # Space: O(n)
        if head is None:
            return True

        ll_array = []
        while(head):
            ll_array.append(head.val)
            head = head.next
        len_array = len(ll_array)
        mid_index = int(len_array / 2)
        if len_array % 2 == 0:
            left_array = ll_array[:mid_index]
            right_array = ll_array[mid_index:][::-1]
            if left_array == right_array:
                return True
        else:
            left_array = ll_array[:mid_index]
            right_array = ll_array[mid_index+1:][::-1]
            if left_array == right_array:
                return True
        return False

        '''
        # Method 2: Find mid-index, revert the second half in-place
        # compare first and second half, revert second half to original
        # Time: O(n)
        # Space: O(1)

        # Traverse till the mid-point of the linked list
        slow, fast = head, head
        while(fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next

        # Slow will be at the end of the left half of the linked list
        # We need to reverse the right half of the linked list

        curr = left.next
        prev = left

        while(curr is not None):
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next

        # prev pointer will be at the end of the linked list
        # Initialize head pointers for first and second half of the linked list
        '''
