import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import list_rotation

@pytest.mark.parametrize("input_list, k, expected", [
  ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
  ([0, 1, 2], 4, [2, 0, 1]),
  ([1, 2], 0, [1, 2]),
  ([1, 2, 3], 3, [1, 2, 3]),
  ([], 1, []),
  ([1, 2, 3, 4], 1, [4, 1, 2, 3]),
  ([10, 20, 30], 2, [20, 30, 10]),
  ([7], 10, [7]),
  ([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3]),
  ([9, 8, 7, 6], 4, [9, 8, 7, 6]),
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

def test_list_rotation(input_list, k, expected):
  list = SingleLinkedList(input_list)
  result = list_rotation(list, k)
  assert str(result) == str(expected)