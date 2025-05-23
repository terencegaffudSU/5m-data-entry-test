import pytest
from src.q1 import *
from src.q2 import *

def test_q1():
    assert swap("Apple", 10) == -1
    assert swap(9, 17) == "The new x is 17 and the new y is 9"

def test_q2():
    assert find_and_replace([1, 2, 3, 4, 2, 2], 2, 5) == [1, 5, 3, 4, 5, 5]
    assert find_and_replace(["apple", "banana", "apple"], "apple", "orange") == ["orange", "banana", "orange"]
