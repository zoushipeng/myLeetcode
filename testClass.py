#!/usr/bin/env python
# coding=utf8


class A(object):
    def __init__(self):
        print "init"

    def __new__(cls, *args, **kwargs):
        print "new %s" % cls
        return object.__new__(cls, *args, **kwargs)


class B(object):
    def __init__(self):
        print "init"

    def __new__(cls, *args, **kwargs):
        print "new %s" % cls
        return object.__new__(cls, *args, **kwargs)


class myClass(A, B):

    def haha(self):
        print 'haha'

    def __init__(self, v):
        print "__init__"
        self.value = v
        print v

    def __new__(cls, *args, **kwargs):
        print "__new__"
        # return object.__new__(cls, *args, **kwargs)
        return super(myClass, cls).__new__(cls, *args, **kwargs)


