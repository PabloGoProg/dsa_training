import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import remove_small_nodes

@pytest.mark.parametrize("input_list, expected", [
  ([5, 2, 13, 3, 8], [13, 8]),
  ([1, 1, 1, 1], [1, 1, 1, 1]),
  ([10, 5, 12, 3, 20], [20]),
  ([7, 6, 5, 4, 3, 2, 1], [7, 6, 5, 4, 3, 2, 1]),
  ([1, 2, 3, 4, 5], [5]),
  ([], []),
  ([9], [9]),
  ([3, 3, 4, 2], [4, 2]),
  ([5, 4, 3, 2, 1, 2, 3, 4, 5], [5, 5]),
  ([1, 3, 2, 4], [4]),
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

def test_remove_small_nodes(input_list, expected):
  list = SingleLinkedList(input_list)
  result = remove_small_nodes(list)
  assert str(result) == str(expected)
