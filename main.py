a = 'Hello'
c = 'ello'
b = 'H' + c
print(id(a), id(b))


def add_one_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 1
    return wrapper


@add_one_decorator
def plus(a):
    return a


print(plus(5))

ex = [x + y for x in range(1,4) for y in range(0, -4, -1)]
print(ex)
