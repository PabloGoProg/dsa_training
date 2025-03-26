import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import bin_to_dec

@pytest.mark.parametrize("input_list, expected", [
  ([1, 0, 1], 5),
  ([0], 0),
  ([1], 1),
  ([1, 1, 1, 1], 15),
  ([1, 0, 0, 1, 1], 19),
  ([1, 0, 0, 0, 0], 16),
  ([0, 1, 1, 0], 6),
  ([1, 1, 0, 1, 0], 26),
  ([1, 0, 1, 0, 1, 0], 42),
  ([1, 1, 1, 0, 0, 1], 57),
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

def test_bin_to_dec(input_list, expected):
    list = SingleLinkedList(input_list)
    result = bin_to_dec(list)
    assert result == expected
