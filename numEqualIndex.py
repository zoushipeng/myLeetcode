#!/usr/bin/env python   
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
一个严格单增的数组，查找a[x] = x的位置

如果a[x] = x存在，那么0 < a[x] < N
a[mid] >= j then res in i~mid-1
a[mid] < j  ok
a[mid] > i  ok
a[mid] <= i then resin i+1 ~ mid

"""