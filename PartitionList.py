#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 86
Given a linked list and a value x, partition it such that all nodes less than x
come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next:
            return "{},{}".format(self.val, self.next)
        else:
            return "{},None".format(self.val)


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        vhead = ListNode(-1)
        vh = vhead
        biger = ListNode(-1)
        hb = biger
        ha = head
        while ha:
            temp = ha
            ha = ha.next
            if temp.val < x:
                vh.next = temp
                vh = vh.next
            else:
                hb.next = temp
                hb = hb.next
        hb.next = None
        vh.next = biger.next
        return vhead.next

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
print head

s = Solution()
print s.partition(head, 3)