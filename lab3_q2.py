def max_product_pair(arr):
    if len(arr) < 2:
        return None

    max_product = float('-inf')
    max_positive = float('-inf')
    min_negative = float('inf')

    for num in arr:
        if num >= 0:
            max_product = max(max_product, num * max_positive)
            max_positive = max(max_positive, num)
            min_negative = min(min_negative, num * min_negative)
        else:
            max_product = max(max_product, num * min_negative)
            min_negative = min(min_negative, num)
            max_positive = max(max_positive, num * max_positive)

    return max_product

size = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
result = max_product_pair(arr)
print("Maximum product pair:", result)
