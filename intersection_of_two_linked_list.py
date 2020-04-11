'''
Write a program to find the node at which the intersection of
two singly linked lists begins.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5],
skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8
(note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5].
From the head of B, it reads as [5,0,1,8,4,5].
There are 2 nodes before the intersected node in A;
There are 3 nodes before the intersected node in B.
 
Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4],
skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2
(note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [0,9,1,2,4].
From the head of B, it reads as [3,2,4].
There are 3 nodes before the intersected node in A;
There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4].
From the head of B, it reads as [1,5].
Since the two lists do not intersect, intersectVal must be 0,
while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Notes:
1. If the two linked lists have no intersection at all, return null.
2. The linked lists must retain their original structure
after the function returns.
3. You may assume there are no cycles anywhere in the entire linked structure.
4. Your code should preferably run in O(n) time and use only O(1) memory.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        # Method 1: Brute Force
        # Pick a node of a list and traverse the other list. Repeat.
        # Time O(mn)
        # Space O(1)

        # Method 2: Hash map
        # Traverse one list and create a Hash map for it
        # Traverse the second list and match the node value if it matches in the hash set
        # Time O(m+n)
        # Space O(m) or O(n)

        '''
        # Method 3: 2 pointers move simultaneosly on both lists
        # If at any point 2 points have the same value, means intersection
        # Also, at the end of traversing, both pointers must be on the same node
        # Time: O(m+n)
        # Space: O(1)

        if headA == None or headB == None:
            return None
        point_A_on_B, point_B_on_A = True, True

        point_A, point_B = headA, headB
        while(point_A and point_B):
            if point_A == point_B:
                return point_A

            if point_A.next == None and point_A_on_B:
                point_A = headB
                point_A_on_B = False
            else:
                point_A = point_A.next

            if point_B.next == None and point_B_on_A:
                point_B = headA
                point_B_on_A = False
            else:
                point_B = point_B.next
        return None
        '''

        # Method 4: Get the difference in lengths of two lists.
        # Give a lead of difference to the pointer of the longer list
        # Then traverse both the pointers to find the intersection node
        # Time: O(m+n)
        # Space: O(1)

        if headA == None or headB == None:
            return None

        point_A, point_B = headA, headB

        # Get individual list lengths
        len_A, len_B = 1, 1
        while(point_A):
            point_A = point_A.next
            len_A += 1

        while(point_B):
            point_B = point_B.next
            len_B += 1

        # Advance the pointer for the longer list
        # First, reset the pointers at the list's heads
        point_A, point_B = headA, headB
        len_diff = abs(len_A - len_B)
        if len_A > len_B:
            for _ in range(len_diff):
                point_A = point_A.next
        else:
            for _ in range(len_diff):
                point_B = point_B.next

        # Traverse both the lists to find the intersection, if any
        while(point_A and point_B):
            if point_A == point_B:
                return point_A
            point_A = point_A.next
            point_B = point_B.next
        return None
