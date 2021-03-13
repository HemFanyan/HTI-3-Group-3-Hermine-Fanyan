import time


def warn_slow(func):
    def inner(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        duration = time.time() - start

        threshold = 2
        if duration > threshold:
            print(f'execution of {func.__name__} with {args}, {kwargs} took more than {threshold} seconds')

        return result
    return inner

@warn_slow
def func_slow(x, y):
    time.sleep(3)

@warn_slow
def func_fast(x, y):
    print(x, y)

func_slow(1, 2)
func_fast(1, 2)
