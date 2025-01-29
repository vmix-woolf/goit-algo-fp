from greedy import greedy_algorithm
from dynamic import dynamic_programming


if __name__ == '__main__':
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 60
    print(f"Budget: {budget}")
    print("Greedy Algorithm:", greedy_algorithm(items, budget))
    print("Dynamic Programming:", dynamic_programming(items, budget))
    print('-' * 40)

    budget = 100
    print(f"Budget: {budget}")
    print("Greedy Algorithm:", greedy_algorithm(items, budget))
    print("Dynamic Programming:", dynamic_programming(items, budget))
    print('-' * 40)

    budget = 140
    print(f"Budget: {budget}")
    print("Greedy Algorithm:", greedy_algorithm(items, budget))
    print("Dynamic Programming:", dynamic_programming(items, budget))