#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 5
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
"""


class Solution(object):
    def isPalindrome(self, str, i, j):
        k = j
        if i < 0 or j >= len(str) or i > j:
            return False
        for i in xrange(i, (j+i)/2+1):
            if str[i] != str[k]:
                return False
            k -= 1
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = 0
        start = 0
        for i in xrange(len(s)):
            if self.isPalindrome(s, i-lens-1, i):
                start = i-lens-1
                lens += 2
            elif self.isPalindrome(s, i-lens, i):
                start = i - lens
                lens += 1
        print start,lens
        return s[start:start+lens]




s = Solution()
print s.longestPalindrome('babad')