import heapq


def dijkstra(graph, start):
    # Ініціалізація
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        # Якщо поточна відстань більша за записану, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Оновлення відстаней до сусідів
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances
