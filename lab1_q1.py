import time
import matplotlib.pyplot as plt

def iterative_sum(N):
    total = 0
    for i in range(1, N + 1):
        total += i
    return total

def recursive_sum(N):
    if N == 0:
        return 0
    return N + recursive_sum(N - 1)

def measure_time(func, N_values):
    times = []
    for N in N_values:
        start_time = time.time()
        func(N)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

N_values = list(range(1, 1001))
iterative_times = measure_time(iterative_sum, N_values)
recursive_times = measure_time(recursive_sum, N_values)

plt.plot(N_values, iterative_times, label='Iterative')
plt.plot(N_values, recursive_times, label='Recursive')
plt.xlabel('N')
plt.ylabel('Time (seconds)')
plt.title('Time taken to compute sum of first N natural numbers')
plt.legend()
plt.show()
