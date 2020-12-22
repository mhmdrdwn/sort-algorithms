# !/usr/local/bin/python
# -*- coding: utf-8 -*-


import random
from algorithms import *

if __name__ == "__main__":
    test_list = list(range(-100,200))
    random.shuffle(test_list)
    assert insertion_sort(test_list) == test_list == sorted(test_list)
    random.shuffle(test_list)
    random.shuffle(test_list)
    assert test_list != sorted(test_list)
    assert bubble_sort(test_list) == test_list == sorted(test_list)
    random.shuffle(test_list)
    assert test_list != sorted(test_list)
    assert combined_sort(test_list) == test_list == sorted(test_list)
    random.shuffle(test_list)
    assert test_list != sorted(test_list)
    assert quick_sort(test_list) == sorted(test_list)
    assert quick_sort(test_list) != test_list
    print('All test passed')
