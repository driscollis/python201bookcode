import urllib.error
import urllib.request

from functools import lru_cache


@lru_cache(maxsize=24)
def get_webpage(module):
    """
    Gets the specified Python module web page
    """
    webpage = "https://docs.python.org/3/library/{}.html".format(module)
    try:
        with urllib.request.urlopen(webpage) as request:
            return request.read()
    except urllib.error.HTTPError:
        return None

if __name__ == '__main__':
    modules = ['functools', 'collections', 'os', 'sys']
    for module in modules:
        page = get_webpage(module)
        if page:
            print("{} module page found".format(module))