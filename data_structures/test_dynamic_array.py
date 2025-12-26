import pytest
from dynamic_array import DynamicArray



def test_starts_empty():
    arr = DynamicArray()
    assert arr.is_empty() is True
    assert arr.length() == 0


def test_append():
    arr = DynamicArray(capacity=3)
    arr.append(10)
    arr.append(20)

    assert arr.length() == 2
    assert arr.index_at(0) == 10
    assert arr.index_at(1) == 20
    assert arr.index_at(2) == None


def test_insert_at_front():
    arr = DynamicArray(capacity=5)
    arr.append(10)
    arr.append(20)

    arr.insert(value=1,index=0)
    assert arr.index_at(0) == 1
    assert arr.index_at(1) == 10
    assert arr.index_at(2) == 20


def test_remove_at_front():
    arr = DynamicArray(capacity=5)
    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.append(40)
    arr.append(50)
    
    arr.remove(index=0)

    assert arr.index_at(0) == 20
    assert arr.index_at(1) == 30
    assert arr.index_at(2) == 40
    assert arr.index_at(3) == None