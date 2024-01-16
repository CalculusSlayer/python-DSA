# binary_recursion.py

def binary_search_recursion(array, target, left_index, right_index):
    if not array or left_index > right_index:
        return -1
    
    mid = left_index + (right_index - left_index) // 2
    if target < array[mid]:
        return binary_search_recursion(array, target, left_index, mid - 1)
    elif target > array[mid]:
        return binary_search_recursion(array, target, mid + 1, right_index)
    else:
        return mid