#!/usr/bin/env python
# coding=utf8
"""
leetcode 41: First Missing Positive
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [num for num in nums if num > 0]
        nums = set(nums)
        for i in xrange(1,len(nums)+2):
            if i not in nums:
                return i

    def firstMissingPositive(self, nums):
        """
        put each num to it's right place.
        ??? worse than the first
        """
        lens = len(nums)
        for i in xrange(lens):
            index = nums[i] - 1
            while (nums[i] > 0) and (nums[i] <= lens) and (nums[index] != nums[i]):
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]
                print i,nums
        for i in xrange(lens):
            if nums[i] != (i + 1):
                return i + 1;
        return lens+1

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
             the range [1,...,l+1] 
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)):
            nums[nums[i]%n]+=n

        for i in range(1,len(nums)):
            if nums[i]/n==0:
                return i
        return n

    def firstMissingPositive(self, nums):
        """
        put each num to it's right place.
        """
        lens = len(nums)
        i = 0
        while(i < lens):
            if i+1 == nums[i]:
                i += 1
            elif nums[i] <=0 or nums[i] > lens or nums[i] == nums[nums[i] - 1]:
                lens -= 1
                nums[i] = nums[lens]
            else:
                t = nums[i]
                nums[i] = nums[t-1]
                nums[t-1] = t
        return lens + 1



s = Solution()
print s.firstMissingPositive([1,3, -1])