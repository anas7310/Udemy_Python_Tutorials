'''
Real-World Example: Multiprocessing for CPU-Bound Tasks
Scenario - Factorial Calculation
Factorial Calculations, especially for large numbers, involve significant computational work, Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performance
'''

import multiprocessing
import time
import math
import sys
#Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

#function to compute factorials of a given numbers
def calculate_factorial(number):
    print(f"Computing Factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000,6000,7000,8000,9000]

    start_time = time.time()
    #create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_factorial, numbers)

    end_time = time.time()

    print(f'Results: {results}')
    print(f'Time taken: {end_time-start_time} seconds')