from functools import wraps, partial
import requests


def retry(func=None, n_tries=3):
    if func is None:
        return partial(retry, n_tries=n_tries)

    @wraps(func)
    def wrapper(*args, **kwargs):
        tries = 0
        while True:
            ret = func(*args, **kwargs)
            if ret.status_code == 500 or ret.status_code == 404 and tries < n_tries:
                print(f"retrying... ({tries})")
                tries += 1
                continue
            break
        return ret

    return wrapper


@retry
def fetch(url):
    resp = requests.get(url)
    return resp


@retry(n_tries=2)
def custom_fetch(url):
    resp = requests.get(url)
    return resp


if __name__ == "__main__":
    url = "https://www.google.com"
    non_existing_url = "https://www.google.com/non-existing-url"

    fetch(url)
    custom_fetch(url)

    print("=" * 60)

    fetch(non_existing_url)
    print("-" * 60)
    custom_fetch(non_existing_url)
