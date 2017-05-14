#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 136
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
s = Solution()
print s.singleNumber([-1, -1, -2])

"""
Given an array of integers,
every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

state
a b c a b
0 0 0 0 0
0 0 1 1 0
1 0 0 1 0
1 0 1 0 1
0 1 0 0 1
0 1 1 0 0


a = 0 表示该数的这一bit出现3次，
a = 1 表示该数这一bit出现1次

变换式：
a = a ^ c & ~b
b = b ^ c & ~a
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for i in nums:
            ones = (ones ^ i) & ~twos
            twos = (twos ^ i) & ~ones
            print bin(ones), bin(twos)
        return ones


s = Solution()
print s.singleNumber([1, 1, 1, 2])

"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

分析：
将所有值抑或，得到结果x ^ y
取结果中bit为1的最低一位。可知x,y在这一位分别为0,1
用这一位做区分，可得到两组数据，各自做抑或，最终得到x,y结果
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = reduce(lambda x, y: x ^ y, nums)
        mask = 1
        while (ans & mask) == 0:
            mask <<= 1
        res = [0, 0]
        for i in nums:
            res[bool(i & mask)] ^= i
        return res


s = Solution()
print s.singleNumber([4, 4, 2, 3])