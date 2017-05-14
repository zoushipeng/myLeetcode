#!/usr/bin/env python
# coding=utf8
"""
leetcode 33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums):
            if nums[0] <= nums[-1]:
                return self._binary_search(nums, 0, len(nums)-1, target)
            else:
                return self._search(nums, 0, len(nums)-1, target)
        return -1

    def _search(self, nums, low, high, target):
        if low < high:
            index = (low+high)/2
            if nums[index] == target:
                return index
            if nums[index] > nums[high]:
                if nums[index] > target and nums[low] <= target:
                    return self._binary_search(nums, low, index, target)
                else:
                    return self._search(nums, index+1, high, target)
            else:
                if nums[index] < target and nums[high] >= target:
                    return self._binary_search(nums, index, high, target)
                else:
                    return self._search(nums, low, index-1, target)
        if low == high:
            if nums[low] == target:
                return low
        return -1

    def _binary_search(self, nums, low, high, target):
        while(low < high):
            index = (low+high)/2
            if nums[index] < target:
                low = index+1
            else:
                high = index
        if nums[high] == target:
            return high
        return -1


s = Solution()
print s.search([1,3],2)