#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
LeetCode 84
Given n non-negative integers representing the histogram's bar height
where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        lens = len(heights)
        stack = []
        right = [0] * lens
        left = [0] * lens
        i = 0
        while i < lens:
            if len(stack) == 0:
                left[i] = -1
                stack.append(i)
                i += 1
                continue
            if heights[stack[-1]] < heights[i]:
                left[i] = stack[-1]
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                right[top] = i

        for i in stack:
            right[i] = stack[-1]+1
        max = 0
        for i in range(len(heights)):
            t = heights[i] * (right[i] - left[i] - 1)
            if t > max:
                max = t
        return max

s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3])