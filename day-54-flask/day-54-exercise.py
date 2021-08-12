import time


def speed_calc_decorator(function):
    def wrapper_function():
        current_time = time.time()
        function()
        finish_time = time.time()
        print(finish_time-current_time)
    return wrapper_function

@speed_calc_decorator
def fast_function():
    print("fast")
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    print("slow")
    for i in range(100000000):
        i * i


fast_function()
slow_function()
