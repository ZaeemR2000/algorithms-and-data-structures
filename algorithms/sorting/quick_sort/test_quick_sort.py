import pytest
from quick_sort import QuickSort

def test_quick_sort_basic():
    sorter = QuickSort()
    nums = [3,2,1,0]
    assert sorter.sort(nums) == [0,1,2,3]


def test_bubble_sort_basic():
    sorter = QuickSort()
    nums = [0,1,2,3]
    assert sorter.sort(nums) == [0,1,2,3]


def test_bubble_sort_duplicate_numbers():
    sorter = QuickSort()
    nums = [0,1,1,2,2,3]
    assert sorter.sort(nums) == [0,1,1,2,2,3]


def test_bubble_sort_neg_numbers():
    sorter = QuickSort()
    nums = [0,-1,-2,3]
    assert sorter.sort(nums) == [-2,-1,0,3]


def test_bubble_sort_flaot():
    sorter = QuickSort()
    nums = [0, 1.2, 2.3, 3, 1.1, 7.9, 0.1]
    assert sorter.sort(nums) == [0, 0.1, 1.1, 1.2, 2.3, 3, 7.9]


def test_bubble_sort_empty():
    sorter = QuickSort()
    nums = []
    assert sorter.sort(nums) == []


def test_bubble_sort_single_element():
    sorter = QuickSort()
    nums = [42]
    assert sorter.sort(nums) == [42]