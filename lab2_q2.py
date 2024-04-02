import heapq

def merge_sorted_lists(sorted_lists):
    heap = []

    for i, lst in enumerate(sorted_lists):
        if lst:  
            heapq.heappush(heap, (lst[0], i, 0))  

    merged_list = []
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        merged_list.append(val)

        if elem_idx + 1 < len(sorted_lists[list_idx]):
            next_val = sorted_lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return merged_list

sorted_lists = [
    [10,20,30,40],
    [15,25,35],
    [27,29,37,48,93],
    [32,33]
]

merged_list = merge_sorted_lists(sorted_lists)
print(merged_list)
