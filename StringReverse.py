# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Assignment using a stack to create string reversal
# Problem solving with Algorithm and Data structures
# Ass 3.43
# a python reverse_STIRNG function to reverse string using stack data structure
# 2:28 31/12/2015


class StackExample(object):
    """ LIFO """
    ''' hacker == rekcah '''

    def __init__(self):
        self.cont = []

    def push(self, item):
        self.cont.insert(0, item)

    def pop(self):
        self.cont.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.cont[-1]

    def items(self):
        return self.cont


def rev_string(string):

    temp = StackExample()
    for i in string:
        temp.push(i)

    return temp.items()

print(rev_string('hacker'))
