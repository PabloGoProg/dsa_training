import sys
import os
import pytest

# Add the path to the data_structures module to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from data_structures import SingleLinkedList
from problems import combine_sorted_lists

@pytest.mark.parametrize("input1, input2, expected", [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0]),
    ([5, 10, 15], [2, 3, 20], [2, 3, 5, 10, 15, 20]),
    ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
    ([1, 2, 3, 4, 5, 6, 7, 8], [9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([-10, -3, 0, 2], [-5, -1, 3], [-10, -5, -3, -1, 0, 2, 3]),
    ([2, 4, 6, 8], [2, 4, 6, 8], [2, 2, 4, 4, 6, 6, 8, 8]),       
    ([1, 2, 3], [10, 20, 30], [1, 2, 3, 10, 20, 30]),
    ([5], [3], [3, 5]),                                              
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
    'Test 10'
])

def test_combine_ordered_lists(input1, input2, expected):
  list1 = SingleLinkedList(input1)
  list2 = SingleLinkedList(input2)
  
  result = combine_sorted_lists(list1, list2)
  
  assert str(result) == str(expected)
