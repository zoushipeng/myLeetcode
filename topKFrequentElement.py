#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 347
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

O(N)
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        times = defaultdict(int)
        for i in nums:
            times[i] += 1
        bucket = defaultdict(list)
        for i in times:
            bucket[times[i]].append(i)
        temp = bucket.keys()
        res = []
        sorted(temp)
        for i in reversed(temp):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res

s = Solution()
print s.topKFrequent([1,1,1,2,2,3], 2)