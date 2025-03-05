import time

def timer_wrapper(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time:.6f} секунд")
        return result
    return wrapper

def prime_generator():
    num = 2
    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

@timer_wrapper
def prime_num_getter(n):
    prime_gen = prime_generator()
    for _ in range(n):
        print(next(prime_gen))


prime_num_getter(10)
