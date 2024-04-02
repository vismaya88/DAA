def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
        else:
            merged_intervals.append(interval)

    return merged_intervals

intervals = [(1, 4), (2, 5), (7,8), (6,9)]
non_overlapping_intervals = merge_intervals(intervals)
print("Non-overlapping intervals after merging:", non_overlapping_intervals)
