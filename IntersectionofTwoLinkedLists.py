#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 160

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ha = headA
        hb = headB
        counta = countb = 0
        while ha:
            ha = ha.next
            counta += 1
        while hb:
            hb = hb.next
            countb += 1
        ha = headA
        hb = headB
        if counta > countb:
            while counta > countb:
                ha = ha.next
                counta -= 1
        elif counta < countb:
            while counta < countb:
                hb = hb.next
                countb -= 1
        while ha and hb:
            if ha == hb:
                return ha
            ha = ha.next
            hb = hb.next
        return None