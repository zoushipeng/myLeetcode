#!/usr/bin/env python
# coding=utf8
"""
leetcode 460: LFU Cache
Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity,
it should invalidate the least frequently used item before inserting a new item.
For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency),
the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?
"""


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import deque, defaultdict
        self.cache = {}
        self.pority = defaultdict(deque)
        self.capacity = capacity
        self.least = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            v, t = self.cache[key]
            self.pority[t].remove(key)
            self.pority[t + 1].appendleft(key)
            self.cache[key] = [v, t + 1]
            if self.least == t and self.pority[t].__len__() == 0:
                self.least = t + 1
            return v
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity > 0:
            if self.get(key) != -1:
                self.cache[key][0] = value
            else:
                if self.capacity <= self.cache.__len__():
                    k = self.pority[self.least].pop()
                    del self.cache[k]
                self.cache[key] = [value, 0]
                self.pority[0].appendleft(key)
                self.least = 0
        return


# Your LFUCache object will be instantiated and called as such:
li1 = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
li2 = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

s1 = [None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,-1,None,None,18,None,None,11,None,None,None,None,None,18,None,None,24,None,4,29,-1,None,12,11,None,None,None,None,29,None,None,None,None,17,-1,18,None,None,None,24,None,None,None,20,None,None,None,29,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
s2 = [None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,14,None,None,18,None,None,11,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,11,None,None,None,None,29,None,None,None,None,17,-1,18,None,None,None,-1,None,None,None,20,None,None,None,29,18,18,None,None,None,None,20,None,None,None,None,None,None,None]

cache = LFUCache(10)
for i in xrange(len(li1)):
    func = getattr(cache, li1[i])
    # if i in range(48):
    #     print cache.cache
    #     print cache.pority
    #     print li1[i],li2[i],cache.least
    ans = func(*li2[i])
    if ans != s2[i]:
        print i
    # if i in range(48):
    #     print ans,s2[i]










