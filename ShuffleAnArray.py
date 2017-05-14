#!/usr/bin/env python
# coding=utf8
"""
leetcode 384. Shuffle an Array
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
class Solution1(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lens = len(nums)
        self.nums = dict()
        for i,num in enumerate(nums):
            self.nums[i] = num

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return [self.nums[i] for i in xrange(self.lens)]        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        from random import choice
        done = range(self.lens)
        res = []
        for i in xrange(self.lens):
            index = choice(done)
            res.append(self.nums[index])
            done.remove(index)
        return res


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lens = len(nums)
        self.nums = nums
        self.res = [num for num in nums]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.res

    def shuffle(self):
        from random import random
        res = self.nums
        for i in reversed(xrange(1, self.lens)):
            j = int(random() * (i+1))
            res[i],res[j] = res[j],res[i]
        return res



obj = Solution([1,2,3])
print obj.reset()
print obj.shuffle()
print obj.reset()
print obj.shuffle()
print obj.reset()