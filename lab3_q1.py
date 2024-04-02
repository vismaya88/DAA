def find_pairs_with_sum(arr, target_sum):
    num_set = set()
    pairs = []
    for num in arr:
        complement = target_sum - num
        if complement in num_set:
            pairs.append((num, complement))
        num_set.add(num)
    return pairs

size = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
target_sum = int(input("Enter the target sum: "))

pairs = find_pairs_with_sum(arr, target_sum)
if pairs:
    print("Pairs with sum", target_sum, "found:", pairs)
else:
    print("No pairs with sum", target_sum, "found in the array.")
