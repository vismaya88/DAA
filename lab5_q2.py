def maximumPeople(n, p, x, m, y, r):
    cloud_coverage = []

    total_population = sum(p)
    max_sunny_population = 0

    covered_population = [0] * n

    for i in range(m):
        cloud_coverage.append((y[i] - r[i], y[i] + r[i]))

    cloud_coverage.sort(key=lambda x: x[1])

    cloud_ptr = 0
    town_ptr = 0

    while town_ptr < n and cloud_ptr < m:
        start, end = cloud_coverage[cloud_ptr]

        while town_ptr < n and x[town_ptr] < start:
            town_ptr += 1

        covered_population_sum = sum(p[town_ptr: min(n, x.index(end) + 1)])
        max_sunny_population = max(max_sunny_population, total_population - covered_population_sum)
        cloud_ptr += 1

    return max_sunny_population

n = int(input())
p = list(map(int, input().split()))  
x = list(map(int, input().split()))  
m = int(input())
y = list(map(int, input().split()))  
r = list(map(int, input().split()))  

print(maximumPeople(n, p, x, m, y, r))
