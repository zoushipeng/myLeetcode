#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 15
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = sorted(nums)
        ans = []
        print res
        for i in xrange(len(res)-2):
            if i > 0 and res[i] == res[i-1]:
                continue
            using = res[i]
            start = i+1
            end = len(res)-1
            while start < end:
                if res[start] + res[end] == -using:
                    ans.append([res[start], res[end], using])
                    t = res[start]
                    while start < len(res) and res[start] == t:
                        start += 1
                    t = res[end]
                    while end > i and res[end] == t:
                        end -= 1
                elif res[start] + res[end] < -using:
                    start += 1
                else:
                    end -= 1
        return ans

s = Solution()
print s.threeSum([0,0,0])


"""
leetcode 16
Given an array S of n integers,
find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = sorted(nums)
        mins = float('Inf')
        ans = target
        for i in xrange(len(res)-2):
            start = i+1
            end = len(res)-1
            while start < end:
                s = res[start] + res[end] + res[i]
                min_t = abs(s - target)
                if min_t < mins:
                    mins = min_t
                    ans = s
                if s == target:
                    return target
                elif s > target:
                    end -= 1
                else:
                    start += 1
        return ans

s= Solution()
print s.threeSumClosest([-1,2,1,-4],1)


"""
leetcode 18
Given an array S of n integers,
are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = sorted(nums)
        ans = []
        print res
        for k in xrange(len(res) - 3):
            if k > 0 and res[k] == res[k - 1]:
                continue
            for i in xrange(k+1, len(res) - 2):
                if k+1 < i < len(res) - 2 and res[i] == res[i-1]:
                    continue
                start = i + 1
                end = len(res) - 1
                while start < end:
                    s = res[start] + res[end] + res[i] + res[k]
                    if s == target:
                        ans.append([res[start], res[end], res[i], res[k]])
                        t = res[start]
                        while start < len(res) and res[start] == t:
                            start += 1
                        t = res[end]
                        while end > i and res[end] == t:
                            end -= 1
                    elif s < target:
                        start += 1
                    else:
                        end -= 1
        return ans

s = Solution()
print s.fourSum([0,0,0,0],0)

"""
leetcode 454 (4sum II)
Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier,
all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^31 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import Counter
        AB = Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)

t = [
[-1,1,1,1,-1],
[0,-1,-1,0,1],
[-1,-1,1,-1,-1],
[0,1,0,-1,-1],
]
s = Solution()
print s.fourSumCount(*t)

# 1 + 1 + 2 + 2 + 6  = 12 * 2
# 6