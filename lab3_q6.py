#a O(n^2) algorithm
def find_pair_with_sum_n2(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                return arr[i], arr[j]
    return None

#b O(nlogn) algorithm
def find_pair_with_sum_nlogn(arr, K):
    arr.sort()  
    left, right = 0, len(arr) - 1
    
    while left < right:
        if arr[left] + arr[right] == K:
            return arr[left], arr[right]
        elif arr[left] + arr[right] < K:
            left += 1
        else:
            right -= 1
    return None

size = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
K = int(input("Enter the value of K: "))

# O(n^2) algorithm result
pair_n2 = find_pair_with_sum_n2(arr, K)
if pair_n2:
    print("O(n^2) Algorithm: Yes, the two numbers that sum up to", K, "are:", pair_n2[0], "and", pair_n2[1])
else:
    print("O(n^2) Algorithm: No pair of numbers found that sum up to", K)

# O(nlogn) algorithm result
pair_nlogn = find_pair_with_sum_nlogn(arr, K)
if pair_nlogn:
    print("O(nlogn) Algorithm: Yes, the two numbers that sum up to", K, "are:", pair_nlogn[0], "and", pair_nlogn[1])
else:
    print("O(nlogn) Algorithm: No pair of numbers found that sum up to", K)
