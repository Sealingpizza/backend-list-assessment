#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie assignment: List2
"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Instructions:
# Complete each of these list manipulation exercises in the same way as the 
# previous List1 excercises.

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
# Hint: Don't use `set()`


def remove_adjacent(nums):
    if(len(nums) < 1):
        return []
    retList = []
    previous = nums[0]
    retList.append(previous)
    for i in nums[1:]:
        if(i != previous):
            previous = i
            retList.append(i)
    return retList


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# The solution should work in "linear" time, making a single pass of both lists.
# Hint: Don't use `sort` or `sorted` -- they are not O(n) linear time, and the two lists
# are already provided in ascending sorted order.
def linear_merge(list1, list2):
    currL1 = 0
    currL2 = 0
    count = len(list1) + len(list2)
    retList = []
    for i in range(0, count):
        if(currL1 == len(list1)):
            retList.append(list2[currL2])
            currL2 += 1
        elif(currL2 == len(list2)):
            retList.append(list1[currL1])
            currL1 += 1
        elif(list1[currL1] < list2[currL2]):
            retList.append(list1[currL1])
            currL1 += 1
        elif(list1[currL1] >= list2[currL2]):
            retList.append(list2[currL2])
            currL2 += 1

    return retList


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}     expected: {}'.format(prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    test(remove_adjacent([2, 2, 3, 3, 3, 4, 5, 2, 3]), [2, 3, 4, 5, 2, 3])

    print('')
    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


# Standard boilerplate (python idiom) to call the main() function.
if __name__ == '__main__':
    main()
