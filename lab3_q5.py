def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0, []

    mid = len(arr) // 2
    left_half, left_count, left_inversions = merge_sort(arr[:mid])
    right_half, right_count, right_inversions = merge_sort(arr[mid:])

    merged_arr = []
    inversion_count = left_count + right_count
    i, j = 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged_arr.append(left_half[i])
            i += 1
        else:
            merged_arr.append(right_half[j])
            j += 1
            inversion_count += len(left_half) - i
            
            for k in range(i, len(left_half)):
                left_inversions.append((left_half[k], right_half[j - 1]))
    merged_arr.extend(left_half[i:])
    merged_arr.extend(right_half[j:])

    return merged_arr, inversion_count, left_inversions + right_inversions

size = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

sorted_arr, inversion_count, inversions = merge_sort(arr)
print("The number of inversions that are possible are as follows:")
print("{", end=" ")
for inv in inversions:
    print("(", inv[0], ",", inv[1], ")", end=" ")
print("}")
print("Total count of inversions:", inversion_count)
