import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import remove_middle_node

@pytest.mark.parametrize("input_list, expected", [
  ([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]),
  ([1, 2, 3, 4], [1, 2, 4]),
  ([2, 1], [2]),
  ([1], []),
  ([5, 10, 15, 20, 25, 30, 35, 40, 45], [5, 10, 15, 20, 25, 30, 40, 45]),
  ([2, 4, 6, 8, 10, 12], [2, 4, 6, 10, 12]),
  ([3, 7], [3]),
  ([9, 8, 7, 6, 5], [9, 8, 6, 5]),
  ([10, 20, 30, 40, 50, 60, 70], [10, 20, 30, 50, 60, 70]),
  ([11, 22, 33, 44], [11, 22, 44]),
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

def test_remove_middle_node(input_list, expected):
  list = SingleLinkedList(input_list)
  result = remove_middle_node(list)
  assert str(result) == str(expected)