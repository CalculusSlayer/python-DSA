"""
playground.py

match statements
https://docs.python.org/3/tutorial/controlflow.html#match-statements

Author: Nayeel Imtiaz
Created on: 06-26-2024
"""

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


def main():
    p1 = (2, 3)

    # p1 is an (x, y) tuple
    match p1:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

    print("*" * 15)
    print(f"400 - {http_error(400)}")
    print(f"404 - {http_error(404)}")
    print(f"418 - {http_error(418)}")
    print(f"555 - {http_error(515)}")
    print(f"620 - {http_error(620)}")
    print(f"401 - {http_error(401)}")

    print("*" * 15)
    where_is(Point(0, 0))
    where_is(Point(0, 3))
    where_is(Point(1, 0))
    where_is(Point(1, 3))
    where_is([2, 5])



if __name__ == '__main__':
    main()
