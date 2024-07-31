# 202040731
# 04:49

def bfs(start_node):
    visited = [-1] * (n + 1)
    visited[start_node] = 0
    queue = [start_node]

    while queue:
        now = queue.pop(0)
        distance = visited[now] + 1

        for next_node in connected[now]:
            if visited[next_node] == -1:
                visited[next_node] = distance
                queue.append(next_node)
            elif visited[next_node] > distance:
                visited[next_node] = distance
                queue.append(next_node)

    return visited[end]


n = int(input())
start, end = map(int, input().split())
e = int(input())
connected = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

print(bfs(start))
