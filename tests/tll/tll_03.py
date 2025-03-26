import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import is_palindrome

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 2, 1], True),
    ([1, 2], False),
    ([1, 0, 1], True),
    ([1, 2, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], False),
    ([1], True),
    ([], True),
    ([1, 1], True),
    ([1, 2, 3, 4, 3, 2, 1], True),
    ([1, 2, 3, 3, 2, 1], True),
], ids=[
    'Test 1',
    'Test 2',
    'Test 3',
    'Test 4',
    'Test 5',
    'Test 6',
    'Test 7',
    'Test 8',
    'Test 9',
    'Test 10',
])

def test_is_palindrome(input_list, expected):
    list = SingleLinkedList(input_list)
    result = is_palindrome(list)
    assert str(result) == str(expected) 
