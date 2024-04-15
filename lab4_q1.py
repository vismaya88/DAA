def fractional_knapsack(items, capacity):
    for item in items:
        item['ratio'] = item['benefit'] / item['weight']
    
    items.sort(key=lambda x: x['ratio'], reverse=True)
    
    total_benefit = 0
    selected_items = []

    for item in items:
        if capacity >= item['weight']:
            selected_items.append((item['id'], 1))  
            total_benefit += item['benefit']
            capacity -= item['weight']
        else:
            fraction = capacity / item['weight']
            selected_items.append((item['id'], fraction))  
            total_benefit += item['benefit'] * fraction
            break  

    return total_benefit, selected_items

items = [
    {'id': 'a', 'benefit': 10, 'weight': 2},
    {'id': 'b', 'benefit': 15, 'weight': 5},
    {'id': 'c', 'benefit': 20, 'weight': 4}
]
capacity = 8

optimal_solution, selected_items = fractional_knapsack(items, capacity)
print("Optimal Solution Benefit:", optimal_solution)
print("Selected Items:", selected_items)
