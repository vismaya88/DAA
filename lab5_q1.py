def candies(n, arr):
    candy_counts = [1] * n

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candy_counts[i] = candy_counts[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candy_counts[i] = max(candy_counts[i], candy_counts[i + 1] + 1)

    total_candies = sum(candy_counts)

    return total_candies, candy_counts

n = int(input("Enter the number of children: "))
arr = list(map(int, input("Enter the ratings of each student (space-separated): ").split()))

total_candies, distribution = candies(n, arr)
print("Total candies:", total_candies)
print("Optimal distribution:", distribution)
