import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import merge_k_ordered_lists

@pytest.mark.parametrize("lists, expected", [
  ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
  ([], []),
  ([[], [1], [0, 2]], [0, 1, 2]),
  ([[2, 3, 7], [1, 4, 6], [0, 9, 10]], [0, 1, 2, 3, 4, 6, 7, 9, 10]),
  ([[-10, -5, 0], [-6, 3, 4], [2]], [-10, -6, -5, 0, 2, 3, 4]),
  ([[1], [2], [3]], [1, 2, 3]),
  ([[1, 3, 5], [2, 4, 6]], [1, 2, 3, 4, 5, 6]),
  ([[1, 1, 1], [1, 1]], [1, 1, 1, 1, 1]),
  ([[]], []),
  ([[0]], [0]),
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

def test_merge_k_ordered_lists(lists, expected):
  lists = [SingleLinkedList(l) for l in lists]
  result = merge_k_ordered_lists(lists, len(lists))
  assert str(result) == str(expected)