# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Problem solving with Data Structures and Algorithms
# Searching .. Linear Search or Sequential Search


def sequential_search(a_list, item):
    found = False
    pos = 0
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found


def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
        return found


def binary_search_r(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_r(a_list[:midpoint], item)
            else:
                return binary_search_r(a_list[midpoint + 1:], item)
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_r(test_list, 3))
print(binary_search_r(test_list, 13))
