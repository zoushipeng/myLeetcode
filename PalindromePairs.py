#!/usr/bin/env python
# coding=utf8
"""
leetcode 336. Palindrome Pairs
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, 
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        for i in xrange(len(words)):
            for j in xrange(len(words)):
                if i == j:
                    continue
                if self._palindrome(words[i]+words[j]):
                    res.append([i,j])
        return res

    def _palindrome(self, word):
        lens = len(word)
        for i in xrange(lens/2):
            if word[i] != word[lens-1-i]:
                return False
        return True

    # Time Limit Exceeded

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = set()
        reverse = {}
        for i in xrange(len(words)):
            reverse[words[i][::-1]] = i
        for i in xrange(len(words)):
            word = words[i]
            for j in xrange(len(word)+1):
                left = word[:j]
                right = word[j:]
                if (left in reverse) and self._palindrome(right) and reverse[left] != i:
                    res.add((i, reverse[left]))
                if (right in reverse) and self._palindrome(left) and reverse[right] != i:
                    res.add((reverse[right], i))

        return [list(r) for r in res]
s = Solution()
print s.palindromePairs(["abcd","dcba","lls","s","sssll"])
# print s._palindrome('abccba')





