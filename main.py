import time


def performance_log(func):
    def decorated_func(*arg, **kwargs):
        start = time.perf_counter()
        print(f"----- hello! -----\n"
              f"start = {start}")
        result = func(*arg, **kwargs)
        stop = time.perf_counter()
        print(f" ---------- \n"
              f"stop: {stop}\n"
              f"elapsed time: {stop - start}")
        return result
    return decorated_func


@performance_log
def long_running_func(num, iters):
    val = 1
    for i in range(iters):
        val *= num
    return val

long_running_func(17, 100000)