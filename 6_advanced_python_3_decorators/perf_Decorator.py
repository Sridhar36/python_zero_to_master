from time import time


def performance(fun):
    ''' this is docstring approach to add comments to a function.
    :param fun: function to be wrapped.
    :return: performance of the function in seconds
    '''
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fun(*args, **kwargs)
        t2 = time()
        print(f'function took {t2 - t1} sec')
        return result

    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()
