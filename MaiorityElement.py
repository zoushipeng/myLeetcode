#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
LeetCode 169
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

思路：
众数个数大于一半，则每次选出两个不同的数X,Y，扔掉，则剩下的数组的众数仍为想要的结果
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            if count == 0:
                ans = i
                count = 1
            elif ans == i:
                count += 1
            else:
                count -= 1
        return ans

s = Solution()
print s.majorityElement([3,3,4])

"""
扩展：如何找到出现次数严格大于总数1/k的数？提示：保存k-1个数。
"""
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = dict()
        delete = []
        for i in nums:
            # res = {k: v for k, v in res.items() if v > 0}
            if i in res:
                res[i] += 1
            else:
                if len(res) < 2:
                    res[i] = 1
                else:
                    for k in res:
                        res[k] -= 1
                        if res[k] == 0:
                            delete.append(k)
                    for k in delete:
                        res.pop(k)
                    delete = []
        for i in res.keys():
            res[i] = 0
            for j in nums:
                if i == j:
                    res[i] += 1
        return [k for k,v in res.items() if v > (len(nums)/3)]


s = Solution()
print s.majorityElement([3,1,4,3,1])
