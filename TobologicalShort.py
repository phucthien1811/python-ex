from collections import defaultdict, deque

def topo_sort(V, edges):
    graph = defaultdict(list)
    indegree = [0] * V

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque([i for i in range(V) if indegree[i] == 0])
    result = []

    while q:
        u = q.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if len(result) == V:
        return result
    else:
        return "Chu trình tồn tại"

edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print(topo_sort(6, edges))  # Output: [4, 5, 2, 3, 1, 0] (có thể khác thứ tự hợp lệ)
