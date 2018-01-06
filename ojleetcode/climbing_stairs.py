"""
알고보니 증가 하는 숫자의 배열이 피보나치와 비슷함.
-  N = (N-1) + (N-2) 를 활용

https://leetcode.com/problems/climbing-stairs/description/
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        two_step_behind = 1
        one_step_behind = 2
        all_ways = 0
        for i in range(n-2):
            all_ways = one_step_behind + two_step_behind
            two_step_behind = one_step_behind
            one_step_behind = all_ways
        return all_ways