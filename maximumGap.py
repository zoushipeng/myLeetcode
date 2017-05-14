#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 164
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

分析：
找到最大值和最小值
将n个元素放入n+1个桶，则必然存在空桶，则最大空隙为空桶左边的最大值到空桶右边的最小值。？？

y - x = (n+1) * d
d = (y-x)/n+1
[x+i*d, x+(i+1)*d)

"""


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        if lens < 2:
            return 0
        mins = maxs = nums[0]
        for i in nums:
            if i > maxs:
                maxs = i
            if i < mins:
                mins = i
        if mins == maxs:
            return 0
        cache = [[0, None, None] for i in xrange(lens+1)]  # empty, maxs, mins
        for i in nums:
            d = lens if maxs == i else (i - mins) * (lens+1) / (maxs - mins)
            if cache[d][0] == 0:  # empty
                cache[d][0] = 1
                cache[d][1] = cache[d][2] = i
            else:                 # not empty
                if i > cache[d][1]:
                    cache[d][1] = i
                if i < cache[d][2]:
                    cache[d][2] = i
        print cache
        res = 0
        flag = False
        max_t = cache[0][1]
        for i in xrange(1, lens+1):
            if cache[i][0]:
                if flag:
                    min_t = cache[i][2]
                    if res < (min_t - max_t):
                        res = (min_t - max_t)
                max_t = cache[i][1]
                flag = False
            else:
                flag = True
        return res

s = Solution()
print s.maximumGap([1,1,1,2])