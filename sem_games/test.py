def dco_a(func):
    def wrapper_a(*args, **kwargs):
        print(func.__name__, args, 'a')
        result = func(*args, **kwargs)
        print(result, 'c')
        return result + 5

    return wrapper_a


def dco_b(func):
    def wrapper_b(*args, **kwargs):
        print(func.__name__, args, 'b')
        result = func(*args, **kwargs)
        print(result, 'd')
        return result

    return wrapper_b


@dco_a
@dco_b
def my_func(*args):
    print('f')
    return sum(args)


print(my_func(5, 3, 4))
