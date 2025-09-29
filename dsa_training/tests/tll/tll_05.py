import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import get_middle_node

@pytest.mark.parametrize("input_list, expected", [
  ([1, 2, 3, 4, 5], [3, 4, 5]),
  ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
  ([1], [1]),
  ([2, 4, 6, 8, 10], [6, 8, 10]),
  ([7, 14, 21, 28, 35, 42, 49], [28, 35, 42, 49]),
  ([1, 2], [2]),
  ([1, 2, 3], [2, 3]),
  ([10, 20, 30, 40], [30, 40]),
  ([0], [0]),
  ([5, 10, 15, 20, 25, 30, 35, 40], [25, 30, 35, 40]),
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

def test_get_middle_node(input_list, expected):
  list = SingleLinkedList(input_list)
  result = get_middle_node(list)
  assert str(result) == str(expected)
