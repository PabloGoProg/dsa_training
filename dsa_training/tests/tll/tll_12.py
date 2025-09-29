import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import point_to_next_bigger_node

@pytest.mark.parametrize("input_list, expected", [
  ([2, 1, 5], [5, 5, 0]),
  ([2, 7, 4, 3, 5], [7, 0, 5, 5, 0]),
  ([1, 7, 5, 1, 9, 2, 5, 1], [7, 9, 9, 9, 0, 5, 0, 0]),
  ([1, 1, 1], [0, 0, 0]),
  ([5, 3, 8, 0, 2], [8, 8, 0, 2, 0]),
  ([1, 2, 3, 4], [2, 3, 4, 0]),
  ([4, 3, 2, 1], [0, 0, 0, 0]),
  ([], []),
  ([2, 2, 3, 1, 4], [3, 3, 4, 4, 0]),
  ([10, 9, 11, 8, 12], [11, 11, 12, 12, 0]),
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

def test_point_to_next_bigger_node(input_list, expected):
  list = SingleLinkedList(input_list)
  result = point_to_next_bigger_node(list)
  assert str(result) == str(expected)