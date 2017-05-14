#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 73
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = set()
        coloum = set()
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    coloum.add(j)
        for i in row:
            for j in xrange(len(matrix[0])):
                matrix[i][j] = 0

        for i in xrange(len(matrix)):
            for j in coloum:
                matrix[i][j] = 0

s = Solution()
s.setZeroes()
