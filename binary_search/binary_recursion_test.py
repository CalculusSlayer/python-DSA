import pytest
import time
from binary_recursion import binary_search_recursion
# look into the 'logging' module if
# you want to print messages w/o
# having to do "pytest -s" or "pytest --capture=no"

def test_standard_binary_search_recursion():
    array1 = [1, 2, 3, 4, 5]
    for index in range(len(array1)):
        assert binary_search_recursion(array1, array1[index], 0, len(array1)-1) == index
    assert binary_search_recursion(array1, 33, 0, len(array1)-1) == -1


def test_single_element_binary_search_recursion():
    single_element_array = [64]
    assert binary_search_recursion(single_element_array, 64, 0, len(single_element_array)-1) == 0
    assert binary_search_recursion(single_element_array, 71, 0, len(single_element_array)-1) == -1


def test_no_elements_binary_search_recursion():
    no_elements_array = []
    assert binary_search_recursion(no_elements_array, 22, 0, len(no_elements_array)-1) == -1


def test_large_array_binary_search_recursion():
    big_array = [number for number in range(int(-1e6), int(1e6))]
    index = 10392
    start_time = time.time()
    result = binary_search_recursion(big_array, big_array[10392], 0, len(big_array)-1)
    end_time = time.time()

    assert result == index, f"Expected {index} but got {result}"
    if end_time - start_time >= 1:
        pytest.fail(f"Binary search took too long: {end_time - start_time} seconds")