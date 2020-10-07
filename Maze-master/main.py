graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
# lista sasiedztwa


def dfs(graph, node):
    print(node)
    visited.update(node)
    for neighbour in graph.get(node):
        if neighbour not in visited:
            dfs(graph, neighbour)


visited = set() # set()
dfs(graph, 'B')