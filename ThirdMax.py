#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 414
Given a non-empty array of integers, return the third maximum number in this array.
 If it does not exist, return the maximum number. The time complexity must be in O(n).
"""


# class Solution(object):
#     def thirdMax(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res = [nums[0]]
#         for i in nums:
#             if i in res:
#                 continue
#             if len(res) < 3:
#                 res.append(i)
#             else:
#                 if i <= min(res):
#                     continue
#                 else:
#                     res.remove(min(res))
#                     res.append(i)
#         if len(res) < 3:
#             return max(res)
#         return min(res)
#
# s = Solution()
# print s.thirdMax([1,2])

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

分析：使用最小堆。nlogk
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums[:k]
        def adjust(heap, pos):
            lens = len(heap)
            childpos = 2*pos + 1
            rightpos = childpos + 1
            max = pos
            if childpos < lens and heap[childpos] < heap[max]:
                max = childpos
            if rightpos < lens and heap[rightpos] < heap[max]:
                max = rightpos
            if max != pos:
                heap[max], heap[pos] = heap[pos], heap[max]
                adjust(heap, max)

        def buildheap(heap):
            lens = len(heap)
            for i in reversed(xrange(lens/2)):
                adjust(heap, i)
                print heap
        buildheap(heap)
        print heap
        for i in xrange(k,len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                adjust(heap, 0)
            print heap
        return heap[0]

s = Solution()
print s.findKthLargest([7,6,5,4,3,2,1], 5)

"""
another way
quickselect
"""

