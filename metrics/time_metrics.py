import time


def measure_computation_time(computation_name, computation, *args):
    start = time.time()
    solution = computation(*args)
    end = time.time()
    print(f"{computation_name} took {end - start}s !")
    return solution




