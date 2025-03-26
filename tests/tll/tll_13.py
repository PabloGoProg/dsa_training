import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import has_cycle

@pytest.mark.parametrize("input_list, pos, expected", [
  ([3, 2, 0, -4], 1, True),
  ([1, 2], 0, True),
  ([1], -1, False),
  ([1, 2, 3, 4, 5], -1, False),
  ([1, 2], -1, False),
  ([1, 2, 3, 4], 2, True),
  ([1, 2, 3, 4, 5, 6], 0, True),
  ([1, 2, 3, 4, 5, 6], 5, True),
  ([], -1, False),
  ([1, 2, 3], 1, True),
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

def test_has_cycle(input_list, pos, expected):
  list = SingleLinkedList(input_list)
  if pos != -1:
    curr = list.head
    for i in range(pos):
      curr = curr.next
    list.tail.next = curr
  result = has_cycle(list)
  assert result == expected