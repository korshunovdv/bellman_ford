def bellman_ford(vertices, edges, start, limit):
    distances = [float('inf')] * vertices
    distances[start] = 0
    for i in range(limit):
        tmp = list(distances)
        for (vertex_from, vertex_to, weight) in edges:
            if distances[vertex_to] > tmp[vertex_from] + weight:
                distances[vertex_to] = tmp[vertex_from] + weight
    return distances


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        vertices, start, finish, limit = map(int, file.readline().split())
        adj_matrix = []
        for _ in range(vertices):
            adj_matrix.append(list(map(int, file.readline().split())))
        edges = []
        for i in range(vertices):
            for j in range(vertices):
                if adj_matrix[i][j] != -1:
                    edges.append((i, j, adj_matrix[i][j]))
    distances = bellman_ford(vertices, edges, start, limit)
    print(distances[finish] if distances[finish] != float('inf') else -1)

