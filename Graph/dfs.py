graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

visited = set()

def dfs(node):

    if node not in visited:

        print(node, end=' ')

        visited.add(node)

        for neighbour in graph[node]:

            dfs(neighbour)

dfs('A')