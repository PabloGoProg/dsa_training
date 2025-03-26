import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import adding_with_lists

@pytest.mark.parametrize("l1, l2, expected", [
  ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
  ([0], [0], [0]),
  ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
  ([1, 8], [0], [1, 8]),
  ([5], [5], [0, 1]),
  ([1, 2, 3], [4, 5, 6], [5, 7, 9]),
  ([9, 9], [1], [0, 0, 1]),
  ([1, 1, 1], [9, 9], [0, 1, 2]),
  ([0, 1], [0, 9, 9], [0, 0, 0, 1]),
  ([2, 0, 1], [9, 9], [1, 0, 2]),
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

def test_adding_with_lists(l1, l2, expected):
  list1 = SingleLinkedList(l1)
  list2 = SingleLinkedList(l2)
  result = adding_with_lists(list1, list2)
  assert str(result) == str(expected)