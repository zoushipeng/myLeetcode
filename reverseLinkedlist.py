#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 92
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        index = 1
        vhead = ListNode(-1)
        vhead.next = head
        ans = vhead
        res = head
        while index < m:
            ans = res
            res = res.next
            index += 1
        ends = res
        res = res.next
        index += 1
        while index <= n:
            temp = res
            index += 1
            res = res.next
            temp.next = ans.next
            ans.next = temp
        ends.next = res
        return vhead.next

    """
    Reverse a singly linked list.

    Hint:
    A linked list can be reversed either iteratively or recursively. Could you implement both?
    """
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        vhead = ListNode(-1)
        vhead.next = head
        ends = head
        while head:
            temp = head
            head = head.next
            temp.next = vhead.next
            vhead.next = temp
        ends.next = None
        return vhead.next

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        t = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return t




head = ListNode(1)
res = head
for i in range(2, 6):
    res.next = ListNode(i)
    res = res.next

print head

# s = Solution()
# print s.reverseList(head)

"""
leetcode 25
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


# Definition for singly-linked list.


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        vhead = ListNode(-1)
        vhead.next = None
        ready = vhead
        while head:
            ends = head
            ready.next = head
            head = head.next
            i = 2
            while i <= k and head:
                temp = head
                head = head.next
                i += 1
                temp.next = ready.next
                ready.next = temp
            ends.next = head
            if i != k+1 and not head:
                temp = ready.next.next
                ends = ready.next
                ends.next = None
                while temp:
                    t = temp
                    temp = temp.next
                    t.next = ready.next
                    ready.next = t
                return vhead.next
            ready = ends
        return vhead.next


# s = Solution()
# print s.reverseKGroup(head, 3)

"""
leetcode 24
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.
"""


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        vhead = ListNode(-1)
        vhead.next = head
        ready = vhead
        while head and head.next:
            ready.next = head.next
            head.next = head.next.next
            ready.next.next = head
            ready = head
            head = head.next
        return vhead.next

s = Solution()
print s.swapPairs(head)
