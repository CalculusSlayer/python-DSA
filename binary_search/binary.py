# binary.py

def binary_search(array, target):
    """
    Vanilla binary search with nothing special

    Parameters:
        array (list[float]): list of floats in ascending order

        target (float): float to search for

    Return:
        (int): Index of found element ([0, len(array) - 1]) or -1 if element was not found
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
    array1 = [1, 2, 3, 4, 5]
    for index in range(len(array1)):
        result = binary_search(array1, array1[index])
        print(f"Array: {array1}, Target: {array1[index]}, result: {result}")
    
    array2 = [64]
    print(f"Array: {array2}, Target: {64}, result: {binary_search(array2, 64)}")

if __name__ == '__main__':
    main()
