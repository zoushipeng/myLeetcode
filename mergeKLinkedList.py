#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 23
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        vhead = ListNode(-1)
        curr = vhead
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return vhead.next

head = ListNode(0)
head.next = ListNode(2)
head.next.next = ListNode(5)
s = Solution()
print s.mergeKLists([head])

