import random
import time
import matplotlib.pyplot as plt

random_numbers = [random.randint(1, 10000) for _ in range(1000)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        index = int((num - min_val) / (max_val - min_val) * (n - 1))
        buckets[index].append(num)
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))
    return result

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

sorting_algorithms = {
    'Bubble Sort': bubble_sort,
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Heap Sort': heap_sort,
    'Quick Sort': quick_sort,
    'Merge Sort': merge_sort,
    'Bucket Sort': bucket_sort,
    'Radix Sort': radix_sort,
}

times = {alg_name: [] for alg_name in sorting_algorithms.keys()}
for alg_name, sorting_algo in sorting_algorithms.items():
    for _ in range(5):  
        arr_copy = random_numbers.copy()
        start_time = time.time()
        sorting_algo(arr_copy)
        end_time = time.time()
        times[alg_name].append(end_time - start_time)

plt.figure(figsize=(12, 8))
for alg_name, time_taken in times.items():
    plt.plot(range(1, 6), time_taken, label=alg_name)
plt.xlabel('Trial')
plt.ylabel('Time (seconds)')
plt.title('Time taken by different sorting algorithms')
plt.xticks(range(1, 6))
plt.legend()
plt.show()
