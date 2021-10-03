from time import perf_counter
from functools import wraps

from logger import logger


def timer(func):
    """This decorator prints out the execution time of a callable."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        ret = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print(f"Finished running {func.__name__} in {run_time:.4f} seconds.")
        return ret

    return wrapper


@logger
@timer
def range_sqrt_sum(n_times):
    return sum((i ** 2 for i in range(n_times)))


if __name__ == "__main__":
    print("Test run 1: ")
    print("Value of Test run 1: ", range_sqrt_sum(10000))
    print("Test run 2: ")
    print("Value of Test run 1: ", range_sqrt_sum(10000000))
