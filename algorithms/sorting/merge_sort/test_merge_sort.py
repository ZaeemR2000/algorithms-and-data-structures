import pytest
from merge_sort import MergeSort

def test_merge_sort_basic():
    sorter = MergeSort()
    nums = [3,2,1,0]
    assert sorter.sort(nums) == [0,1,2,3]


def test_merge__sort_duplicate_numbers():
    sorter = MergeSort()
    nums = [0,1,1,2,2,3]
    assert sorter.sort(nums) == [0,1,1,2,2,3]


def test_merge__sort_neg_numbers():
    sorter = MergeSort()
    nums = [0,-1,-2,3]
    assert sorter.sort(nums) == [-2,-1,0,3]


def test_merge__sort_flaot():
    sorter = MergeSort()
    nums = [0, 1.2, 2.3, 3, 1.1, 7.9, 0.1]
    assert sorter.sort(nums) == [0, 0.1, 1.1, 1.2, 2.3, 3, 7.9]