from timeit import Timer

setup_code = """
import numpy as np
SIZE = 100_000
"""

codes = [
    '''my_list = [i for i in range(SIZE)]''',
    '''my_list = list(i for i in range(SIZE))''',
    '''my_list = [*range(SIZE)]''',
    '''my_list = list(range(SIZE))''',
    '''my_list = np.array(range(SIZE))''',
    '''my_list = np.arange(SIZE)''',
]

for code in codes:
    t = Timer(code, setup_code)
    print(code)
    print(t.timeit(100))
    print('-' * 20)

