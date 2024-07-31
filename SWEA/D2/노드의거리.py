# 20240731
# 09:33

def bfs(start_node):
    queue = [(start_node, 0)]
    visited = [-1] * (v + 1)
    visited[start_node] = 1

    while queue:
        now, distance = queue.pop()  # pop(0)해야 BFS임.
        if now == end:
            continue

        distance += 1
        for next_node in connected[now]:
            if visited[next_node] == -1:
                visited[next_node] = distance
                queue.append((next_node, distance))
            elif visited[next_node] > distance:  # bfs로 풀었으면 이 코드 필요 없는데, 위에 queue.pop()으로 dfs로 해서 필요한 코드 됨.
                visited[next_node] = distance
                queue.append((next_node, distance))

    return visited[end]


T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    connected = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        connected[a].append(b)
        connected[b].append(a)
    start, end = map(int, input().split())

    answer = bfs(start)

    print(f"#{test_case} {0 if answer == -1 else answer}")
