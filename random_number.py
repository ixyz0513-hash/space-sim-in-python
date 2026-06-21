import time


def random_number_generator(mins,maxs):

    seed = time.time_ns()
    
    a: int = 16643434
    c: int = 10139043232
    m: int = 2**32

    next_seed = (a * seed + c) % m
    if type(mins) == int:
        min_max_size = maxs - mins + 1
    else:
        min_max_size = maxs - mins + 0.001
    value = (next_seed % min_max_size) + mins
    return value
