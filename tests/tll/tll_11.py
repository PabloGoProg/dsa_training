import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import reorder_list

@pytest.mark.parametrize("input_list, expected", [
  ([1, 2, 3, 4], [1, 4, 2, 3]),
  ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
  ([1], [1]),
  ([1, 2], [1, 2]),
  ([10, 20, 30, 40, 50, 60], [10, 60, 20, 50, 30, 40]),
  ([], []),
  ([2, 2, 2, 2], [2, 2, 2, 2]),
  ([1, 3, 5, 7, 9, 11, 13], [1, 13, 3, 11, 5, 9, 7]),
  ([0, 1, 2, 3, 4], [0, 4, 1, 3, 2]),
  ([100, 200, 300], [100, 300, 200]),
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

def test_reorder_list(input_list, expected):
  list = SingleLinkedList(input_list)
  result = reorder_list(list)
  assert str(result) == str(expected)

