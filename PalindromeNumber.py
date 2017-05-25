#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
LeetCode 9
Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer.
However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        t = x
        lens = 0
        while t:
            lens += 1
            t /= 10
        while lens > 0:
            m = pow(10, lens-1)
            if x/m != x%10:
                return False
            lens -= 2
            x = (x % m) / 10
        return True

s = Solution()
print s.isPalindrome(13131)