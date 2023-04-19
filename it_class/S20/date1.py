import time 
import random

l1 = [random.randint(1, 99999) for i in range(1000)]
now = time.time()


start = time.perf_counter_ns()
l1.sort()
stop = time.perf_counter_ns()

print(f"Executia a durat {stop - start} s.")