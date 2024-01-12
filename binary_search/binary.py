# binary.py
import random

def binary_search(array, target):
    """
    Vanilla binary search with nothing special

    Parameters:
        array (list[float]): list of floats in ascending order

        target (float): float to search for

    Return:
        (int): Index of found element ([0, len(array) - 1]) or -1 if element was not found
    
    TC: O(log n) where n is number of elements in array
    SC: O(1)
    """

    left_index, right_index = 0, len(array) - 1
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        if array[mid_index] > target:
            right_index = mid_index - 1
        elif array[mid_index] < target:
            left_index = mid_index + 1
        else:
            return mid_index
    
    return -1

def main():
    random.seed(42)

    array1 = [1, 2, 3, 4, 5]
    for index in range(len(array1)):
        result = binary_search(array1, array1[index])
        print(f"Array: {array1}, Target: {array1[index]}, result: {result}")
    print(f"Array: {array1}, Target: {33}, result: {result}")
    print()
    
    single_element_array = [64]
    print(f"Array: {single_element_array}, Target: {64}, result: {binary_search(single_element_array, 64)}")
    print(f"Array: {single_element_array}, Target: {71}, result: {binary_search(single_element_array, 71)}")
    print()

    no_elements_array = []
    print(f"Array: {no_elements_array}, Target: {24}, result: {binary_search(no_elements_array, 24)}")

    random_array = sorted([random.randrange(5) for random_number in range(20)])
    print(random_array)

    print(f"Array: {random_array}, Target: {4}, result: {binary_search(random_array, 4)}")

if __name__ == '__main__':
    main()
