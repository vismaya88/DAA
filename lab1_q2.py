import time
import random
import matplotlib.pyplot as plt

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_time(search_func, arr, key):
    start_time = time.time()
    search_func(arr, key)
    end_time = time.time()
    return end_time - start_time

arr = generate_random_array(10000)
keys = []

for i in range(5):
    key = int(input(f"Enter search key {i+1}: "))
    keys.append(key)

linear_times = []
binary_times = []

for key in keys:
    linear_times.append(measure_time(linear_search, arr, key))
    binary_times.append(measure_time(binary_search, sorted(arr), key))

plt.plot(keys, linear_times, label='Linear Search')
plt.plot(keys, binary_times, label='Binary Search')
plt.xlabel('Search Key')
plt.ylabel('Time (seconds)')
plt.title('Time taken by Linear and Binary Search for 5 different search keys')
plt.legend()
plt.show()
