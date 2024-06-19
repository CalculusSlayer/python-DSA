"""
june_14_24.py

Simple Python functions and test cases to assert they work as intended.

Author: Nayeel Imtiaz
Created on: 06-14-2024
"""

def calculator(num1, num2, operation):
    """
    1) Simple Calculator:

    Create a function calculate that takes three parameters: num1, num2, and operation.
    The operation parameter should be a string that can be "add", "subtract", "multiply", 
    or "divide".
    Based on the operation, return the result of applying it to num1 and num2.
    """
    if not isinstance(num1, (int, float)):
        raise TypeError
    if not isinstance(num2, (int, float)):
        raise TypeError
    if operation not in ["add", "substract", "multiply", "divide"]:
        raise TypeError("operation parameter is not valid")

    if operation == "add":
        return num1 + num2
    if operation == "substract":
        return num1 - num2
    if operation == "multiply":
        return num1 * num2
    if operation == "divide":
        return num1 / num2


def modify_list(list1):
    '''
    2) Write a function modify_list that takes a list of numbers.
    The function should return a new list containing only the even numbers 
    from the original list, each multiplied by 2.
    '''
    if not isinstance(list1, list):
        raise TypeError
    if len(list1) > 0 and not isinstance(list1[0], int):
        raise TypeError

    new_list = []
    for number in list1:
        if number % 2 == 0:
            new_list.append(number * 2)

    return new_list


def main():
    """This is main function"""
    print("*" * 10 + "Testing calculator function" + "*" * 10)
    print()
    assert calculator(3, 2, "add") == 5
    assert calculator(3, 2, "substract") == 1
    assert calculator(3, 2, "multiply") == 6
    assert calculator(3, 2, "divide") == 1.5

    try:
        calculator("a", 1, "add")
        assert False, "Expected TypeError"
    except TypeError:
        assert True

    try:
        calculator(2, "b", "add")
        assert False, "Expected TypeError"
    except TypeError:
        assert True

    try:
        calculator(2, 3, "not an operation")
        assert False, "Expected TypeError"
    except TypeError:
        assert True

    print("*" * 10 + "Testing modify_list function" + "*" * 10)
    print()
    assert modify_list([1, 2, 3, 4]) == [4, 8]
    assert modify_list([1, 3]) == []
    assert modify_list([2, 4, 0]) == [4, 8, 0]
    assert modify_list([-3, -4]) == [-8]

    try:
        modify_list(24)
        assert False, "Expected TypeError"
    except TypeError:
        assert True

    try:
        modify_list(["apple"])
        assert False, "Expected TypeError"
    except TypeError:
        assert True


if __name__ == '__main__':
    main()
