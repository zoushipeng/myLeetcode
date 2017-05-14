#!/usr/bin/env python
# coding=utf8
"""
leetcode 93. Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
    	lens = len(s)
    	for i in [1,2,3]:
    		if (lens-i < 3) or (lens-i > 9) or (self.true_ip(s[:i]) == False):
    			continue
    		for j in [1,2,3]:
    			if lens-i-j < 2 or lens-i-j > 6 or self.true_ip(s[i:i+j]) == False:
    				continue
    			for k in [1,2,3]:
    				if (lens-i-j-k >= 1) and (lens-i-j-k <= 3) and (self.true_ip(s[i+j:i+j+k]) == True) and (self.true_ip(s[i+j+k:]) == True):
    					res.append('.'.join([s[:i], s[i:i+j], s[i+j:i+j+k], s[i+j+k:]]))
        return res

    def true_ip(self,s):
    	t = int(s)
    	if t == 0 and len(s) == 1:
    		return True
    	if t<=255 and t>0 and s[0]!='0':
    		return True
    	return False


s = Solution()
print s.restoreIpAddresses("010010")
print s.true_ip("01")



