import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import reverse

@pytest.mark.parametrize("input_list, expected", [
  ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
  ([1, 2], [2, 1]),
  ([1], [1]),
  ([], []),
  ([3, 7, 9, 10], [10, 9, 7, 3]),
  ([1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1]),
  ([0, 0, 0], [0, 0, 0]),
  ([1, -1], [-1, 1]),
  ([10], [10]),
  ([8, 2, 4, 6], [6, 4, 2, 8]),
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

def test_reverse(input_list, expected):
  list = SingleLinkedList(input_list)
  result = reverse(list)
  assert str(result) == str(expected)