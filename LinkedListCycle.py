#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 141

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}".format(self.val)
        # if self.next:
        #     return "{},{}".format(self.val, self.next)
        # else:
        #     return "{},None".format(self.val)


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        fast = head
        slow = head
        while fast and slow:
            if slow.next:
                slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break
            if slow == fast:
                return True
        return False

    """
    leetcode 142
    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

    Note: Do not modify the linked list.

    Follow up:
    Can you solve it without using extra space?
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        fast = head
        slow = head
        while fast and slow:
            if slow.next:
                slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break
            if slow == fast:
                slow = head
                if slow == fast:
                    return slow
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    if slow == fast:
                        return slow

        return None



head = ListNode(3)
head.next = head
# head.next = two = ListNode(2)
# head.next.next = zero = ListNode(0)
# head.next.next.next = four = ListNode(-4)
# four.next = two

s = Solution()
print s.detectCycle(head)



