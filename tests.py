import pytest
from src.q1 import *
from src.q2 import *
from src.q3 import *
from src.q4 import *
from src.q5 import *
from src.q6 import *
from src.q7 import *

def test_q1():
    assert swap("Apple", 10) == -1
    assert swap(9, 17) == "The new x is 17 and the new y is 9"

def test_q2():
    assert find_and_replace([1, 2, 3, 4, 2, 2], 2, 5) == [1, 5, 3, 4, 5, 5]
    assert find_and_replace(["apple", "banana", "apple"], "apple", "orange") == ["orange", "banana", "orange"]

def test_q3():
    assert update_dictionary({}, "name", "Alice") == {"name":"Alice"}
    assert update_dictionary({"age": 25}, "age", 26) == {"age": 26}

def test_q4():
    assert string_reverse("Hello World") == "dlroW olleH"
    assert string_reverse("Python") == "nohtyP"

def test_q5():
    assert check_divisibility(10, 2) == True
    assert check_divisibility(7, 3) == False

def test_q6():
    assert find_first_negative([3, 5, -1, 7, -2, 8]) == -1
    assert find_first_negative([2, 10, 7, 0]) == "No negatives"

def test_q7():
    newCar = Car("Toyota", "Corolla", "2020")
    assert newCar.describe_car() == "2020 Toyota Corolla"