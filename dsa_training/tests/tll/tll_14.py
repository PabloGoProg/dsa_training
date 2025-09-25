import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import remove_nth_last_node

@pytest.mark.parametrize("input_list, n, expected", [
  ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
  ([1], 1, []),
  ([1, 2], 1, [1]),
  ([1, 2, 3], 3, [2, 3]),
  ([10, 20, 30, 40], 4, [20, 30, 40]),
  ([1, 2, 3, 4], 1, [1, 2, 3]),
  ([1, 2, 3, 4], 4, [2, 3, 4]),
  ([1, 2, 3, 4, 5, 6], 3, [1, 2, 3, 5, 6]),
  ([1, 1, 1, 1], 2, [1, 1, 1]),
  ([2, 3], 2, [3]),
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

def test_remove_nth_last_node(input_list, n, expected):
  list = SingleLinkedList(input_list)
  result = remove_nth_last_node(list, n)
  assert str(result) == str(expected)