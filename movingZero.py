#!/usr/bin/env python
# coding=utf8
"""
leetcode 283  : moving zeros
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        high = len(nums) - 1
        for i in reversed(range(len(nums))):
            if nums[i] == 0:
                temp = i
                while high > temp:
                    nums[temp] = nums[temp+1]
                    temp += 1

                nums[high] = 0
                high -= 1
        print nums

    def moveZeroes(self, nums):
        j=0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1
        for i in range(j,len(nums)):
            nums[i] = 0
        print nums


s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])


