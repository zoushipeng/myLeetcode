#!/usr/bin/env python
# coding=utf8
"""
leetcode 330. Patching Array
Given a sorted positive integer array nums and an integer n, add/patch elements to the array 
such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. 
Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
"""
class Solution(object):
	def minPatches(self, nums, n):
		"""
		:type nums: List[int]
		:type n: int
		:rtype: int
		"""
		count = 0
		cache = set()
		for num in nums:
			self._cache_add(cache, num)
		for i in xrange(1,n+1):
			if i not in cache:
				self._cache_add(cache, i)
				count += 1
		return count


	def _cache_add(self, cache, num):
		temp = [c for c in cache]
		for c in temp:
			cache[c+num] = True
		cache.add(num)

    # time limit exceeed
    # [1,2,31,33],2147483647

    def minPatches(self, nums, n):
    	"""
    	1,2,4,...,2**n 可实现 2**(n+1)-1内的所有数字 
    	"""
    	mi = self._mi(n)
    	mi_set = range(mi+1)

    	cache = dict()
    	for t in nums:
    		self._cache_add(cache,t)

    	reach = [0,0]
    	for i in mi_set:
    		if (2**i) in cache:
    			reach[1] += 2**(i+1)-1
    		else:




    	return 0



    def _mi(self,num):
    	"""
    	2 ** n <= num < 2 ** (n+1)
    	求n
    	"""
    	count = 0
    	while(num/2 > 0):
    		count += 1
    		num /= 2
    	return count



s = Solution()
print s.minPatches([2,4,14,18,20,25,25,35,73,94],42)
# print s._mi(5)



        		











