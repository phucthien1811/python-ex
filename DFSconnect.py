def connected_components(graph):
    visited = set()
    components = []

    def dfs(u, comp):
        visited.add(u)
        comp.append(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v, comp)

    for node in graph:
        if node not in visited:
            comp = []
            dfs(node, comp)
            components.append(comp)
    return components

graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: []
}
print(connected_components(graph))  # Output: [[0, 1], [2, 3], [4]]
