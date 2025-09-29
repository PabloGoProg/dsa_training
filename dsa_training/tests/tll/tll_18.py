import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import reverse_groups_of_nodes

@pytest.mark.parametrize("input_list, k, expected", [
  ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
  ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
  ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),
  ([1, 2, 3, 4], 4, [4, 3, 2, 1]),
  ([1, 2, 3], 1, [1, 2, 3]),
  ([1, 2, 3, 4, 5, 6, 7], 3, [3, 2, 1, 6, 5, 4, 7]),
  ([1, 2, 3, 4, 5, 6, 7, 8], 2, [2, 1, 4, 3, 6, 5, 8, 7]),
  ([1, 2, 3, 4, 5, 6], 1, [1, 2, 3, 4, 5, 6]),
  ([1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1]),
  ([], 3, []),
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

def test_reverse_groups_of_nodes(input_list, k, expected):
  list = SingleLinkedList(input_list)
  result = reverse_groups_of_nodes(list, k)
  assert str(result) == str(expected)