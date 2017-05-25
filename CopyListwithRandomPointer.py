#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 138
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __repr__(self):
        return "{}".format(self.label)


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        ha = head
        while ha:
            temp = RandomListNode(ha.label)
            temp.next = ha.next
            ha.next = temp
            ha = ha.next.next
        ha = head
        while ha:
            if ha.random:
                ha.next.random = ha.random.next
            ha = ha.next.next
        ha = head
        vhead = ha.next
        vh = vhead
        while ha:
            ha.next = vh.next
            ha = ha.next
            if ha:
                vh.next = ha.next
                vh = vh.next
        return vhead


