'''
The Fibonacci numbers, commonly denoted F(n) form a sequence,
called the Fibonacci sequence, such that each number is the sum of the
two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).

Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:
0 ≤ N ≤ 30.
'''


class Solution:
    def fib(self, N: int) -> int:
        '''
        # Solution 1
        if N == 0:
            return 0
        if N == 1:
            return 1

        memo = {0:0, 1:1}
        for num in range(2, N+1):
            if (N-1) not in memo:
                add_1 = self.fib(N-1)
                memo[N-1] = add_1
            else:
                add_1 = memo[N-1]

            if (N-2) not in memo:
                add_2 = self.fib(N-2)
                memo[N-2] = add_2
            else:
                add_2 = memo[N-2]
        return add_1 + add_2
        '''
    # Solution 2
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.memoize(N)

    def memoize(self, N):
        memo = {0: 0, 1: 1}

        for num in range(2, N+1):
            memo[num] = memo[num - 1] + memo[num - 2]
        return memo[N]
