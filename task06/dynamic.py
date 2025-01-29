def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost, calories = info["cost"], info["calories"]
        for b in range(budget + 1):
            if cost > b:
                dp[i][b] = dp[i - 1][b]
            else:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)

    # Відновлення вибору страв
    selected_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name, info = item_list[i - 1]
            selected_items.append(name)
            b -= info["cost"]

    return selected_items, dp[n][budget]