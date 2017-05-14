#!/usr/bin/env python
# coding=utf8
"""
leetcode 493. Reverse Pairs
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:
Input: [1,3,2,3,1]
Output: 2

Example2:
Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in xrange(len(nums)):
        	for j in xrange(i+1,len(nums)):
        		if nums[i] > 2*nums[j]:
        			count+=1
        return count
        # Time Limit Exceeded

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        from collections import defaultdict
        index = defaultdict(list)
        for i in xrange(len(nums)):
        	index[self._two_nums(nums[i])].append([nums[i],i])
        
        for i in xrange(len(nums)):
        	s = self._two_nums(nums[i])
        	for j in index.keys():
        		if j >= s-1:continue
        		for v,t in index[j]:
        			if t > i:count+=1
        	for v,t in index[s-1]:
        		if nums[i] > 2*v and i < t:count+=1
        	if nums[i] <0:
        		for v,t in index[s]:
        			if nums[i] > 2*v and i < t:count+=1

       	print index
        return count
        #  Time Limit Exceeded


    def _two_nums(self, num):
    	if num <=0:
    		return -1
    	count = 0
    	num -= 1
    	while(num/2):
    		num/=2
    		count+=1
    	return count

s = Solution()
print s.reversePairs([2,4,3,5,1])

# print s._two_nums(9)







