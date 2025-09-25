import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import swap_in_pairs

@pytest.mark.parametrize("input_list, expected", [
  ([1, 2, 3, 4], [2, 1, 4, 3]),
  ([1, 2, 3], [2, 1, 3]),
  ([1], [1]),
  ([], []),
  ([5, 9, 8, 3, 7], [9, 5, 3, 8, 7]),
  ([1, 2], [2, 1]),
  ([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]),
  ([10, 20, 30, 40, 50], [20, 10, 40, 30, 50]),
  ([0, 1], [1, 0]),
  ([7, 7, 7, 7], [7, 7, 7, 7]),
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

def test_swap_in_pairs(input_list, expected):
  list = SingleLinkedList(input_list)
  result = swap_in_pairs(list)
  assert str(result) == str(expected)