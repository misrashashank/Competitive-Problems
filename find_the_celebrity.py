'''
Suppose you are at a party with n people (labeled from 0 to n - 1) and
among them, there may exist one celebrity.
The definition of a celebrity is that all the other n - 1 people know him/her
but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one.
The only thing you are allowed to do is to ask questions
like: "Hi, A. Do you know B?" to get information of whether A knows B.
You need to find out the celebrity (or verify there is not one) by asking as
few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether
A knows B. Implement a function int findCelebrity(n). 
There will be exactly one celebrity if he/she is in the party.
Return the celebrity's label if there is a celebrity in the party.
If there is no celebrity, return -1.

Example 1:
Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2.
graph[i][j] = 1 means person i knows person j,
otherwise graph[i][j] = 0means person i does not know person j.
The celebrity is the person labeled as 1 because both 0 and 2 know him
but 1 does not know anybody.

Example 2:
Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.

Note:
The directed graph is represented as an adjacency matrix,
which is an n x n matrix where a[i][j] = 1 means person i knows person j
while a[i][j] = 0 means the contrary.
Remember that you won't have direct access to the adjacency matrix.
'''


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    '''
    # Brute Force approach
    # Check for each celebrity if it is a celebrity or not

    def findCelebrity(self, n: int) -> int:
        # Brute force approach
        self.n = n

        if n == 0:
            return -1

        for item in range(self.n):
            if self.check_celebrity(item):
                return item
        return -1

    def check_celebrity(self, person):
        for other in range(self.n):
            if other == person:
                continue
            else:
                if not knows(other, person) or knows(person, other):
                    return False
        return True
    '''

    def findCelebrity(self, n: int) -> int:
        # Graph approach
        # Find a probable celebrity, then check
        # Person is celebrity if it satisfies both conditions:
        # 1. (n-1) inbound edges
        # 2. 0 outbound edge
        # Reduce number of candidate celebrities for checking condition
        # As above approach checks for each person whether it is a celebrity
        # or not, this approach first finds the optimum candidate
        # and then checks the condition

        self.n = n
        if n == 0:
            return -1

        person = 0
        for other in range(1, self.n):
            if knows(person, other):
                person = other
        if self.check_celebrity(person):
            return person
        return -1

    def check_celebrity(self, person):
        for other in range(self.n):
            if person != other:
                if knows(person, other) or not knows(other, person):
                    return False
        return True
