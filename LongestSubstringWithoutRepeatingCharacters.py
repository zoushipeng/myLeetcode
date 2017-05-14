#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 3
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import deque
        exist = set()
        cache = deque()
        a = list(s)
        ans = j = 0
        while(j < len(a)):
            if a[j] not in exist:
                exist.add(a[j])
                cache.append(a[j])
                if ans < len(cache):
                    ans = len(cache)
            else:
                t = cache.popleft()
                while t != a[j]:
                    exist.remove(t)
                    t = cache.popleft()
                exist.remove(t)
                exist.add(a[j])
                cache.append(a[j])
            j += 1
        return ans

s = Solution()
print s.lengthOfLongestSubstring("aab")