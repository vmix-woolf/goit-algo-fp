import random


def generate_graph(num_vertices, num_edges):
    """
    Генерує випадковий граф з num_vertices вершинами та num_edges ребрами.
    Ваги ребер випадкові (від 1 до 10).
    """
    if num_edges > num_vertices * (num_vertices - 1) // 2:
        raise ValueError("Занадто багато ребер для заданої кількості вершин")

    graph = {i: [] for i in range(num_vertices)}  # Ініціалізація графа
    edges_added = 0

    while edges_added < num_edges:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        weight = random.randint(1, 10)  # Випадкова вага ребра

        # Додаємо ребро, якщо воно не існує і не є петлею
        if u != v and (v, weight) not in graph[u]:
            graph[u].append((v, weight))
            graph[v].append((u, weight))  # Для неорієнтованого графа
            edges_added += 1

    return graph
