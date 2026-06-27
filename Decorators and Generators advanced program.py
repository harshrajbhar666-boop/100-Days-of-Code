import time


def time_logger(func):
    def wrapper(*args, **kwargs):
        print("⏱️  Time tracking started...")
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        print(f"⏱️  Time tracking finished. Took {end_time - start_time:.6f} seconds.")
        print("-" * 40)
        return result
    return wrapper


@time_logger
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


if __name__ == "__main__":
    print("--- Running Merged Advanced Program ---\n")
    
    
    fib_nums = fibonacci_generator(5)
    
    print("Printing generated numbers:")
    for num in fib_nums:
        print(f"➡️ Generated: {num}")