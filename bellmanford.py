def bellman_ford(edges, V, start):
    dist = [float('inf')] * V
    dist[start] = 0

    for _ in range(V-1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Kiểm tra chu trình âm
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return "Chu trình âm tồn tại"
    return dist

edges = [(0, 1, 4), (0, 2, 5), (1, 2, -3), (2, 3, 4)]
print(bellman_ford(edges, 4, 0))  # Output: [0, 4, 1, 5]
