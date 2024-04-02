import heapq

def k_largest(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    
    for num in arr[k:]:
        if num > heap[0]:
            heapq.heappop(heap)  
            heapq.heappush(heap, num)  
    
    return heap

arr = [3, 10, 4, 7, 9, 12, 5]
k = int(input("Enter the value of k: "))
k_largest = k_largest(arr, k)
print("K largest elements:", k_largest)
