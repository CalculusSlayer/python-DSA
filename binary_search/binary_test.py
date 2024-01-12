import pytest
import time
from binary import binary_search
# look into the 'logging' module if
# you want to print messages w/o
# having to do "pytest -s" or "pytest --capture=no"

def test_standard_binary_search():
    array1 = [1, 2, 3, 4, 5]
    for index in range(len(array1)):
        assert binary_search(array1, array1[index]) == index
    assert binary_search(array1, 33) == -1


def test_single_element_binary_search():
    single_element_array = [64]
    assert binary_search(single_element_array, 64) == 0
    assert binary_search(single_element_array, 71) == -1


def test_no_elements_binary_search():
    no_elements_array = []
    assert binary_search(no_elements_array, 22) == -1


def test_large_array_binary_search():
    big_array = [number for number in range(int(-1e6), int(1e6))]
    index = 10392
    start_time = time.time()
    result = binary_search(big_array, big_array[10392])
    end_time = time.time()

    assert result == index, f"Expected {index} but got {result}"
    if end_time - start_time >= 1:
        pytest.fail(f"Binary search took too long: {end_time - start_time} seconds")