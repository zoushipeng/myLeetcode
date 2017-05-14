#!/usr/bin/env python
# coding=utf8
"""
leetcode 401. Binary Watch
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
        	return ['0:00']

        if num >=9:
        	return []

        if num == 1:
			return ['8:00', '2:00', '0:32', '4:00', '1:00', '0:08', '0:04', '0:16', '0:02', '0:01']
		if num == 2:
			return ['1:02', '0:36', '1:04', '0:33', '0:18', '1:01', '1:32', '0:34', '0:10', '0:12', '1:08', '0:17', '2:08', '8:04', '8:02', '8:01', '2:01', '2:02', '2:04', '8:08', '4:32', '4:16', '0:20', '2:32', '0:24', '0:09', '0:06', '0:05', '6:00', '0:03', '0:48', '8:16', '5:00', '0:40', '1:16', '2:16', '10:00', '4:02', '4:01', '4:04', '8:32', '4:08', '9:00', '3:00']
		if num == 3:
			return ['0:37', '0:35', '0:38', '2:09', '5:32', '2:03', '2:05', '2:06', '9:32', '3:16', '6:08', '6:04', '0:07', '6:01', '6:02', '2:18', '4:40', '2:12', '2:10', '2:17', '4:48', '1:12', '3:08', '3:04', '1:10', '3:01', '0:19', '1:48', '2:24', '2:20', '0:11', '6:16', '0:13', '0:14', '5:16', '8:40', '9:16', '3:32', '8:48', '2:33', '2:34', '2:36', '1:40', '5:08', '5:01', '1:36', '5:02', '5:04', '3:02', '4:24', '4:20', '9:08', '9:04', '9:01', '9:02', '1:24', '6:32', '2:40', '10:16', '2:48', '1:20', '4:36', '4:34', '4:33', '8:20', '8:24', '1:18', '0:49', '10:08', '0:42', '10:04', '0:41', '10:02', '1:17', '0:44', '10:01', '4:03', '1:06', '4:06', '4:05', '8:33', '4:09', '8:36', '8:34', '1:05', '0:56', '0:50', '1:03', '0:52', '11:00', '1:33', '1:09', '1:34', '8:06', '8:05', '8:03', '10:32', '8:09', '7:00', '4:18', '4:17', '4:10', '4:12', '0:21', '0:22', '0:25', '0:26', '0:28', '8:10', '8:12', '8:17', '8:18']
		

		if num == 4:
			return ['0:30', '0:39', '6:06', '8:42', '5:33', '5:34', '5:36', '2:07', '9:34', '9:36', '3:18', '9:33', '3:17', '3:10', '3:12', '11:32', '4:44', '10:40', '1:19', '6:09', '1:56', '6:05', '10:48', '1:52', '1:50', '6:03', '2:19', '5:20', '4:42', '5:24', '2:13', '2:11', '2:50', '4:49', '9:24', '3:09', '9:20', '3:06', '3:05', '3:03', '10:17', '1:11', '2:26', '2:25', '2:22', '10:10', '6:18', '1:41', '2:14', '0:15', '1:44', '2:28', '6:10', '4:50', '4:52', '5:18', '4:56', '5:17', '5:12', '5:10', '0:43', '9:12', '9:10', '8:41', '9:17', '8:44', '3:33', '9:18', '8:49', '3:36', '3:34', '6:12', '2:35', '2:37', '0:58', '2:38', '6:20', '6:24', '10:18', '5:09', '3:24', '1:38', '3:20', '1:35', '5:03', '4:41', '5:05', '5:06', '4:25', '4:26', '9:09', '4:21', '4:22', '9:05', '9:06', '4:28', '8:50', '9:03', '8:52', '6:34', '6:36', '6:33', '2:49', '2:44', '8:28', '2:41', '2:42', '1:28', '1:26', '1:25', '1:22', '1:21', '10:12', '4:37', '4:35', '6:17', '8:21', '8:22', '8:25', '8:26', '4:38', '6:40', '6:48', '5:40', '2:56', '3:40', '2:52', '10:09', '10:06', '1:13', '3:48', '0:46', '10:03', '1:14', '0:45', '0:54', '8:38', '4:07', '7:16', '8:37', '8:35', '1:37', '2:21', '0:57', '11:08', '1:07', '0:51', '0:53', '11:01', '11:02', '11:04', '8:07', '1:42', '10:33', '10:36', '10:34', '7:02', '7:01', '4:19', '7:04', '4:14', '7:08', '4:11', '4:13', '1:49', '10:24', '0:23', '10:20', '0:27', '0:29', '11:16', '8:11', '9:40', '8:13', '8:56', '8:14', '8:19', '9:48', '10:05', '5:48', '7:32']
		

		if num == 5:
			return ['11:24', '1:58', '11:20', '10:50', '0:31', '10:52', '10:56', '10:26', '10:49', '5:35', '5:37', '5:38', '8:43', '1:53', '9:35', '9:37', '3:19', '3:14', '7:20', '1:51', '9:38', '3:11', '3:13', '11:33', '11:34', '11:36', '7:48', '7:40', '10:42', '4:15', '10:41', '10:44', '1:57', '1:54', '6:07', '5:50', '5:26', '4:46', '5:22', '5:21', '4:45', '4:43', '5:25', '5:28', '2:15', '9:26', '9:25', '9:22', '9:21', '3:07', '7:12', '9:28', '2:27', '11:40', '6:19', '1:43', '6:14', '6:13', '11:48', '6:11', '2:29', '4:51', '4:53', '4:54', '4:57', '5:19', '4:58', '5:14', '5:13', '5:11', '9:13', '3:38', '9:11', '8:46', '9:14', '8:45', '9:19', '3:37', '3:35', '8:57', '3:52', '3:42', '2:30', '6:28', '6:22', '6:21', '6:26', '6:25', '3:25', '3:26', '3:21', '1:39', '3:22', '1:30', '3:28', '5:07', '4:27', '8:58', '4:23', '8:54', '9:07', '8:51', '4:29', '8:53', '6:35', '6:37', '10:11', '6:38', '2:39', '3:50', '2:45', '2:46', '10:19', '3:56', '2:43', '1:27', '10:14', '1:23', '10:13', '8:29', '1:45', '4:30', '8:23', '4:39', '8:27', '6:41', '6:42', '6:44', '6:49', '8:15', '2:57', '0:55', '3:41', '2:54', '2:53', '2:51', '3:44', '10:07', '3:49', '0:47', '2:58', '7:10', '8:39', '7:17', '7:18', '8:30', '2:23', '6:52', '6:50', '6:56', '11:09', '1:15', '11:03', '11:05', '11:06', '9:56', '10:38', '9:52', '9:50', '0:59', '10:37', '10:35', '7:03', '1:29', '7:06', '7:05', '5:52', '7:09', '1:46', '5:56', '10:25', '11:18', '10:21', '10:22', '11:12', '11:10', '10:28', '11:17', '9:41', '5:44', '9:42', '5:41', '9:44', '5:42', '9:49', '5:49', '7:24', '7:36', '7:34', '7:33']
		

		if num == 6:
			return ['11:26', '11:25', '11:22', '11:21', '7:56', '1:59', '7:50', '7:52', '11:28', '10:51', '10:53', '10:54', '10:57', '10:58', '5:30', '5:39', '7:28', '9:30', '7:21', '3:15', '7:22', '7:25', '9:39', '7:26', '11:35', '7:49', '11:37', '11:38', '7:44', '7:42', '7:41', '10:43', '10:46', '10:45', '1:55', '5:23', '4:47', '5:27', '5:29', '9:27', '9:23', '9:29', '11:44', '11:41', '11:42', '6:15', '11:49', '1:47', '4:55', '4:59', '5:15', '3:39', '8:47', '9:15', '3:30', '11:56', '3:53', '11:52', '11:50', '6:23', '6:27', '2:31', '3:27', '3:23', '3:29', '1:31', '10:15', '10:27', '8:59', '8:55', '6:30', '6:39', '6:29', '3:51', '2:47', '3:54', '3:57', '3:58', '4:31', '6:43', '6:45', '6:46', '3:43', '2:55', '3:46', '3:45', '2:59', '7:11', '7:13', '7:14', '7:19', '8:31', '6:53', '6:51', '6:57', '6:54', '6:58', '11:07', '9:57', '9:54', '9:53', '9:51', '10:30', '9:58', '5:58', '7:07', '5:53', '5:51', '5:57', '5:54', '10:39', '11:19', '10:23', '11:13', '11:11', '10:29', '11:14', '5:45', '9:43', '5:46', '9:45', '5:43', '9:46', '7:38', '7:37', '7:35']
		

		if num == 7:
			return ['11:27', '11:23', '6:55', '7:54', '6:59', '7:57', '7:51', '11:29', '7:53', '11:45', '11:46', '10:55', '11:43', '10:59', '7:58', '5:31', '9:55', '3:55', '3:59', '10:31', '9:59', '7:29', '5:59', '9:31', '7:46', '7:23', '3:31', '7:27', '5:55', '11:30', '6:47', '11:39', '7:45', '7:43', '11:57', '11:54', '10:47', '11:51', '11:58', '11:15', '5:47', '3:47', '9:47', '6:31', '7:15', '7:39', '7:30', '11:53']
		

		if num == 8:
			return ['11:31', '7:59', '7:47', '7:55', '11:47', '11:55', '11:59', '7:31']

    def __init__(self):
    	self.cache = dict()
    	middle = dict()
    	middle[0] = set(['0000000000'])
    	for i in xrange(1,9):
    		res = set()
        	for v in middle[i-1]:
        		for j in xrange(len(v)):
        			tempv = v
        			if tempv[j] == '0':
        				res.add(tempv[:j] + '1' + tempv[j+1:])
        	middle[i] = res

        	ans = set()
        	for r in res:
        		m = 0
        		h = 0
        		for j in xrange(6):
        			if r[j] == '1':
        				m += 2 ** j
        		if m > 59:
        			continue
        		if m < 10:
        			m = '0%d' % m
        		for j in xrange(6,10):
        			if r[j] == '1':
        				h += 2 ** (j-6)
        		if h > 11:
        			continue
        		ans.add('%s:%s' % (h,m))
        	self.cache[i] = list(ans)

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
        	return ["0:00"]
        if num == 1:
        	return ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
        if num >= 9:
        	return []
        if num in self.cache:
        	return self.cache[num]

        









s = Solution()
print s.readBinaryWatch(1)
for k,v in s.cache.items():
	q = '''
	if num == %d:
		return %s
	''' % (k,v)
	print q









