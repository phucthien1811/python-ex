def tarjans_scc(graph):
    n = len(graph)
    index = [0]
    indices = [-1]*n
    lowlink = [-1]*n
    stack = []
    on_stack = [False]*n
    sccs = []

    def strongconnect(v):
        indices[v] = lowlink[v] = index[0]
        index[0] += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for v in range(n):
        if indices[v] == -1:
            strongconnect(v)

    return sccs

graph = [[1], [2], [0, 3], [4], [5], [3]]
print(tarjans_scc(graph))  # Output: [[2, 1, 0], [5, 4, 3]]
