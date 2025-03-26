import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import combine_between_zeros

@pytest.mark.parametrize("input_list, expected", [
  ([0, 3, 1, 0, 4, 5, 2, 0], [4, 11]),
  ([0, 1, 0, 3, 0, 2, 2, 0], [1, 3, 4]),
  ([0, 5, 0], [5]),
  ([0, 10, 20, 30, 0, 40, 0], [60, 40]),
  ([0, 7, 8, 0, 1, 2, 3, 0], [15, 6]),
  ([0, 1, 2, 0, 3, 4, 0, 5, 6, 0], [3, 7, 11]),
  ([0, 9, 9, 9, 0], [27]),
  ([0, 1, 1, 1, 1, 0], [4]),
  ([0, 100, 200, 300, 0, 400, 500, 0], [600, 900]),
  ([0, 5, 5, 5, 5, 0], [20]),
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

def test_combine_between_zeros(input_list, expected):
  list = SingleLinkedList(input_list)
  result = combine_between_zeros(list)  
  assert str(result) == str(expected)