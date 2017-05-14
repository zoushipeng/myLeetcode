#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
LeetCode 153
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""


# class Solution(object):
#     def findMin(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         lens = len(nums)
#         i, j = 0, lens-1
#         while i < j:
#             if nums[j] > nums[i]:
#                 return nums[i]
#             mid = (i + j) / 2
#             if mid == i or mid == j:
#                 return min(nums[i], nums[j])
#             if nums[mid] < nums[i]:
#                 i += 1
#                 j = mid
#             else:
#                 i = mid + 1
#
#         return nums[i]

# s = Solution()
# print s.findMin([1, 2, 0, 1, 1, 1, 1])

"""
leetcode 154
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        i, j = 0, lens-1
        while i < j:
            if nums[j] > nums[i]:
                return nums[i]
            mid = (i + j) / 2
            if mid == i or mid == j:
                return min(nums[i], nums[j])
            if nums[mid] < nums[i]:
                i += 1
                j = mid
            elif nums[mid] > nums[i]:
                i = mid + 1
            else:
                t = nums[mid]
                k = i
                while k < lens and nums[k] == t:
                    k += 1
                if k >= mid:
                    i = mid + 1
                else:
                    j = mid
                    i += 1

        return nums[i]

s = Solution()
print s.findMin([1, 1, 1])
