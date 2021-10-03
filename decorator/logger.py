from functools import wraps


def print_divider():
    print("=" * 60)


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print_divider()
        print(f"Running function: {func.__name__}")
        ret = func(*args, **kwargs)
        print(f"Finished function: {func.__name__}")
        print_divider()
        return ret

    return wrapper
