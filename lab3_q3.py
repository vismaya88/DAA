def sort_array_with_swapped_elements(arr):
    first_element = None
    second_element = None
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            first_element = arr[i]
            break
    for j in range(len(arr) - 1, 0, -1):
        if arr[j] < arr[j - 1]:
            second_element = arr[j]
            break

    first_index = arr.index(first_element)
    second_index = arr.index(second_element)
    
    arr[first_index], arr[second_index] = arr[second_index], arr[first_index]
    
    return arr

arr = [3,8,6,7,5,9]
sorted_arr = sort_array_with_swapped_elements(arr)
print("Sorted array:", sorted_arr)
