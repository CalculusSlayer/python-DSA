# june 11, 2024

user_input = input('enter smt: ')

# expect user to enter a float

# print(f"user_input = {user_input}, type = {type(user_input)}")

try:
    print(float(user_input))
except ValueError:
    print("User did not enter a float.")