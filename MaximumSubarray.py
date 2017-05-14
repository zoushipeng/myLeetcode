#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 53
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_t = nums[0]
        for i in nums:
            sum += i
            max_t = max(max_t, sum)
            sum = max(0, sum)
        return max_t
    # 动态规划
    # maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i];
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        dp.append(nums[0])
        max_t = nums[0]
        for i in range(1, len(nums)):
            t = dp[i-1] if dp[i-1] > 0 else 0
            dp.append(t + nums[i])
            if dp[i] > max_t:
                max_t = dp[i]
        return max_t

s = Solution()
print s.maxSubArray([-9,-2,1,8,7,-6,4,9,-9,-5,0,5,-2,5,9,7])
