"""
1) Simple Calculator:

Create a function calculate that takes three parameters: num1, num2, and operation.
The operation parameter should be a string that can be "add", "subtract", "multiply", or "divide".
Based on the operation, return the result of applying it to num1 and num2.
List Manipulation:

2) Write a function modify_list that takes a list of numbers.
The function should return a new list containing only the even numbers from the original list, each multiplied by 2.
String Reversal Checker:

3) Create a function is_palindrome that checks if a given string is a palindrome (a word that reads the same forwards and backwards).
Ignore casing and spaces in the string.
"""
def calculator(num1, num2, operation):
    if not isinstance(num1, (int, float)):
        raise TypeError
    if not isinstance(num2, (int, float)):
        raise TypeError
    if operation not in ["add", "substract", "multiply", "divide"]:
        raise TypeError("operation parameter is not valid")
    
    if operation == "add":
        return num1 + num2
    elif operation == "substract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2


def modify_list(list1):
    '''
    2) Write a function modify_list that takes a list of numbers.
    The function should return a new list containing only the even numbers 
    from the original list, each multiplied by 2.
    '''
    
    new_list = []
    for number in list1:
        if number % 2 == 0:
            new_list.append(number * 2)
    
    return new_list
    

def main():
    print('this is main')

    # # Testing calculator
    # assert calculator(3, 2, "add") == 5
    # assert calculator(3, 2, "substract") == 1
    # assert calculator(3, 2, "multiply") == 6
    # assert calculator(3, 2, "divide") == 1.5

    # calculator("a", 1, "add")

if __name__ == '__main__':
    main()