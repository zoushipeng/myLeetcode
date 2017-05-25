#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 239
Given an array nums, there is a sliding window of size k
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

分析：可维护最大堆，时间复杂度O(NlogK) ??
2、采用滑动窗口，利用双端队列，可实现O(N)
"""


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        lens = len(nums)
        res = [0] * lens
        cache = deque()
        for i in xrange(lens):
            if len(cache) >0 and cache[0] <= i-k:
                cache.popleft()
            if len(cache)==0:
                cache.append(i)
                res[i] = nums[i]
                continue
            while len(cache)>0 and nums[cache[-1]] < nums[i]:
                cache.pop()
            cache.append(i)
            res[i] = nums[cache[0]]
        return res[k-1:]

s = Solution()
print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
