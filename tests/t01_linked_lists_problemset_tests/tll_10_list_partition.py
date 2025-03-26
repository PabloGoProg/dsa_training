import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import list_partition

@pytest.mark.parametrize("input_list, x, expected", [
  ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
  ([2, 1], 2, [1, 2]),
  ([1, 2, 3], 4, [1, 2, 3]),
  ([3, 5, 8, 5, 10, 2, 1], 5, [3, 2, 1, 5, 8, 5, 10]),
  ([], 1, []),
  ([1, 3, 2, 4, 3, 2, 5], 3, [1, 2, 2, 3, 4, 3, 5]),
  ([5, 1, 8, 0, 3], 4, [1, 0, 3, 5, 8]),
  ([2, 2, 2], 2, [2, 2, 2]),
  ([1, 4, 2, 5, 3], 3, [1, 2, 4, 5, 3]),
  ([10, 9, 8, 7, 6, 5], 8, [7, 6, 5, 10, 9, 8]),
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

def test_list_partition(input_list, x, expected):
  list = SingleLinkedList(input_list)
  result = list_partition(list, x)
  assert str(result) == str(expected)