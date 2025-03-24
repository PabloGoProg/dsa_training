import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import delete_duplicates

@pytest.mark.parametrize("input_list, expected", [
    ([1, 1, 2], [1, 2]),
    ([1, 1, 2, 3, 3], [1, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 1, 1, 1, 1], [1]),
    ([], []),
    ([4, 2, 2, 1, 1], [4, 2, 1]),
    ([10, -5, -5, 0, 3, 3, 3, 8], [10, -5, 0, 3, 8]),
    ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
    ([5, 1, 2, 2, 1, 5, 4, 3, 3, 4], [1, 2, 3, 4, 5]),
    ([0, -1, -1, -1, 0, 1, 1, 2, 2], [-1, 0, 1, 2]),
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
    'Test 10'
])

def test_delete_duplicates(input_list, expected):
  list = SingleLinkedList(input_list)
  
  result = delete_duplicates(list)
  
  assert str(result) == str(expected)