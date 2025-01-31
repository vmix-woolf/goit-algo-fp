import matplotlib.pyplot as plt
import random

# Кількість симуляцій
N = 1_000_000

# Можливі суми від 2 до 12
sums_count = {i: 0 for i in range(2, 13)}

# Симуляція кидків двох кубиків
for _ in range(N):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll_sum = dice1 + dice2
    sums_count[roll_sum] += 1

# Обчислення ймовірностей
simulated_probabilities = {k: (v / N) * 100 for k, v in sums_count.items()}

# Теоретичні ймовірності з таблиці в домашньому завданні
theoretical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}

# Вивід результатів
print("Сума | Симульована ймовірність (%) | Теоретична ймовірність (%)")
for i in range(2, 13):
    print(f" {i:2d}  | {simulated_probabilities[i]:27.2f} | {theoretical_probabilities[i]:2.2f}")

# Візуалізація
plt.figure(figsize=(10, 5))
plt.bar(simulated_probabilities.keys(), simulated_probabilities.values(), alpha=0.6, label="Метод Монте-Карло")
plt.plot(theoretical_probabilities.keys(),
         theoretical_probabilities.values(),
         marker="o",
         color="r",
         linestyle="--",
         label="Теоретичні ймовірності")

plt.xlabel("Сума на двох кубиках")
plt.ylabel("Ймовірність (%)")
plt.title("Порівняння симуляції Монте-Карло та теоретичних ймовірностей")
plt.xticks(range(2, 13))
plt.legend()
plt.show()
