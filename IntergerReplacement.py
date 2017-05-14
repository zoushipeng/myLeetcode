#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 397
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?
***01 -1
***11 +1
"""
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 1:
            if n == 3:
                n -= 1
                count += 1
            if n & 1 == 0:
                n /= 2
            elif n & 2 == 0:
                n -= 1
            else:
                n += 1
            count += 1
        return count

s= Solution()
print s.integerReplacement(3)

