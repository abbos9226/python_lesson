import concurrent.futures
import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a given range."""
    return [n for n in range(start, end) if is_prime(n)]

def parallel_prime_check(start, end, num_threads=4):
    """Check for prime numbers in a range using multiple threads."""
    step = (end - start) // num_threads
    ranges = [(start + i * step, start + (i + 1) * step) for i in range(num_threads)]
    
    # Ensure the last range extends to the end
    ranges[-1] = (ranges[-1][0], end)

    primes = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(lambda r: find_primes_in_range(*r), ranges)
    
    for result in results:
        primes.extend(result)
    
    return sorted(primes) 

start_range = 1
end_range = 100
num_threads = 4

primes = parallel_prime_check(start_range, end_range, num_threads)
print(f"Prime numbers between {start_range} and {end_range}: {primes}")
