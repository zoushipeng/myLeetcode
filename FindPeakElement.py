#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 162
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while i < j:
            mid = (i + j) / 2
            if mid == i or mid == j:
                return i if nums[i] > nums[j] else j
            if nums[mid] > nums[mid+1]:
                j = mid
            else:
                i = mid + 1
        return i
s = Solution()
print s.findPeakElement([1,2,3,1])