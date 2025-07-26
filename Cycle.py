def has_cycle(graph):
    visited = set()
    stack = set()

    def dfs(v):
        visited.add(v)
        stack.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in stack:
                return True
        stack.remove(v)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

g = {0: [1], 1: [2], 2: [0]}  # Có chu trình
print(has_cycle(g))  # True
