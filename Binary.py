# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Algorithm and Data Structures with python
# Decimal to Binary converter

from Stackexample import Bstack


def divide_by_2(dec_number):

    rem_stack = Bstack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)

        dec_number = dec_number // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


def base_converter(dec_number, base):
    """
       A decimal to binary convertion function using 
       the divide_by_2 Algorithm 
       this function converts from any base to binary 
       -Implemented usign the stack data structure 
    """

    digits = "0123456789ABCDEF"

    rem_stack = Bstack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)

        dec_number = dec_number // base

    new_string = ""

    while not rem_stack.is_empty():

        new_string = new_string + digits[rem_stack.pop()]

    return new_string

# print(base_converter(25,2))
print(base_converter(26, 26))
