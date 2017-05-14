#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 2
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

means
342 + 465 = 807
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1
        b = l2
        val = a.val + b.val
        if val >= 10:
            flag = 1
            val -= 10
        else:
            flag = 0
        res = ListNode(val)
        ans = res
        while a.next and b.next:
            a = a.next
            b = b.next
            val = a.val + b.val + flag
            if val >= 10:
                flag = 1
                val -= 10
            else:
                flag = 0
            next = ListNode(val)
            res.next = next
            res = res.next
        while(a.next):
            a = a.next
            val = a.val + flag
            if val >= 10:
                flag = 1
                val -= 10
            else:
                flag = 0
            next = ListNode(val)
            res.next = next
            res = res.next
        while (b.next):
            b = b.next
            val = b.val + flag
            if val >= 10:
                flag = 1
                val -= 10
            else:
                flag = 0
            next = ListNode(val)
            res.next = next
            res = res.next
        if flag:
            res.next = ListNode(1)
        return ans

s= Solution()
a = ListNode(5)

b = ListNode(5)

res = s.addTwoNumbers(a, b)
while(res):
    print res.val
    res = res.next

