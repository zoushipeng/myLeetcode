#!/usr/bin/env python
# coding=utf8
"""
leetcode 448. Find All Numbers Disappeared in an Array
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lens = len(nums)
        nums = set(nums)
        res = []
        for i in xrange(1,lens+1):
        	if i not in nums:
        		res.append(i)
        return res

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
        	if nums[abs(nums[i])-1] > 0:
        		nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

        return [ i+1 for i in xrange(len(nums)) if nums[i] > 0]



s = Solution()
print s.findDisappearedNumbers([1,1])




