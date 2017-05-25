#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
leetcode 155
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.p1 = []
        self.p2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.p1.append(x)
        if len(self.p2) == 0 or self.p2[-1] >= x:
            self.p2.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if self.p1[-1] == self.p2[-1]:
            self.p2.pop()
        self.p1.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.p1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.p2[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()