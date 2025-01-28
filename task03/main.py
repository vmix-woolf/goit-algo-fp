from djikstra_alg import dijkstra
from graph import generate_graph


if __name__ == '__main__':
    # Параметри графа
    num_vertices = 5  # Кількість вершин
    num_edges = 7  # Кількість ребер

    # Генерація графа
    graph = generate_graph(num_vertices, num_edges)
    print("Згенерований граф (список суміжності):")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {neighbors}")

    # Виклик алгоритму Дейкстри
    start_vertex = 0 # Початкова вершина
    shortest_paths = dijkstra(graph, start_vertex)
    print(f"\nНайкоротші шляхи від вершини {start_vertex}: {shortest_paths}")