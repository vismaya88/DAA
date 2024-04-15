def pylons(k, arr):
    n = len(arr)
    plants = 0
    i = 0
    
    while i < n:
        j = min(i + k - 1, n - 1)
        while j >= max(0, i - k + 1) and arr[j] == 0:
            j -= 1
        
        if j < max(0, i - k + 1):
            return -1
        
        plants += 1
        i = j + k
    
    return plants

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(pylons(k, arr))
