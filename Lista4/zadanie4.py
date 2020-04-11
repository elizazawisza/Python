import math
from inspect import getfullargspec


class FunctionOverloadingDecorator:
    given_functions = {}

    def __init__(self, function):
        self.function_name = function.__name__
        self.given_functions[
            (function.__name__, len(getfullargspec(function).args))] = function

    def __call__(self, *args, **kwargs):
        return self.given_functions[self.function_name, len(args)](*args, **kwargs)


def overload(function):
    return FunctionOverloadingDecorator(function)


@overload
def norm(x, y):
    return math.sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


@overload
def circuit(r):
    return 2 * math.pi * r


@overload
def circuit(a, b):
    return 2 * a + 3 * b


@overload
def circuit(a, b, c):
    return a + b + c


if __name__ == '__main__':
    print(f"norm(2,4) = {norm(2, 4)}")
    print(f"norm(2,3,4) = {norm(2, 3, 4)}")

    print(f"Circle circuit (r=5) = {circuit(5)}")
    print(f"Rectangle circuit (a=8, b=4) = {circuit(8, 4)}")
    print(f"Triangle circuit (a=5, b=12, c=13) = {circuit(5, 12, 13)}")
