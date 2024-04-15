arr=[2,5,3,4,0]

def max_sum(arr):
    arr.sort()
    n=len(arr)
    result=sum(arr[i]*i for i in range(n))
    return result

maximized_sum = max_sum(arr)
print("Maximum sum:", maximized_sum)