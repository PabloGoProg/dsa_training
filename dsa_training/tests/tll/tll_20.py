import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import odd_even_lists

@pytest.mark.parametrize("input_list, expected", [
  ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
  ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
  ([1, 2, 3, 4], [1, 3, 2, 4]),
  ([1], [1]),
  ([10, 20, 30, 40, 50, 60], [10, 30, 50, 20, 40, 60]),
  ([], []),
  ([2, 4], [2, 4]),
  ([9, 8, 7], [9, 7, 8]),
  ([5, 3, 1, 2, 4, 6, 8], [5, 1, 4, 8, 3, 2, 6]),
  ([100, 200, 300, 400, 500], [100, 300, 500, 200, 400]),
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

def test_odd_even_lists(input_list, expected):
  list = SingleLinkedList(input_list)
  result = odd_even_lists(list)
  assert str(result) == str(expected)
