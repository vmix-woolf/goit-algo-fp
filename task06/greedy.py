def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    selected_items = []

    for name, info in sorted_items:
        if budget >= info["cost"]:
            selected_items.append(name)
            total_calories += info["calories"]
            budget -= info["cost"]

    return selected_items, total_calories
