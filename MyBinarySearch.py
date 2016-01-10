# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# THIS IS MY VERSION OF THE BINARY SEARCH IMPLEMENTATION
# 1/9/2016
# 10: 03 PM

mlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]


def new_binary_search(userlist, item):
    found = False
    first = 0
    last = -1
    midpoint = len(userlist) // 2

    if item <= userlist[midpoint]:
        # go left cos its lesser
        last = midpoint  # change last to the midpoint
        for items in userlist[first:last]:
            if items == item:
                found = True
    else:
        # go right
        first = midpoint  # change first to refer to midpoint
        for items in userlist[first:last]:
            if items == item:
                found = True
    return found


def recursive_binary(userlist, item):
    if len(userlist) == 0:
        return False
    else:
        midpoint = len(userlist) // 2
        if userlist[midpoint] == item:
            return True
        else:
            if item < userlist[midpoint]:
                return recursive_binary(userlist[:midpoint], item)
            else:
                return recursive_binary(userlist[midpoint + 1:], item)

print(recursive_binary(mlist, 8))
