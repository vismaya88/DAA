def max_activities(activities):
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    selected_activities = [sorted_activities[0]]
    
    for activity in sorted_activities[1:]:
        start_time, _ = activity
        if start_time >= selected_activities[-1][1]:
            selected_activities.append(activity)
    
    return selected_activities

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
selected_activities = max_activities(activities)
print("Maximum number of activities performed by a single person:", len(selected_activities))
print("Selected activities:", selected_activities)
