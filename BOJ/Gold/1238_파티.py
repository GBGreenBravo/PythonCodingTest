# 20240818
# 12:19
# 1 / 1

from collections import deque


def dijkstra(start, connected_arr):  # 다익스트라; 최단 경로 찾기
    visited = [1e9] * (n + 1)  # start에서 각 노드들로의 최단 거리 저장할 배열
    visited[start] = 0
    queue = deque([start])

    while queue:
        now = queue.popleft()
        time = visited[now]
        for next_node, next_time in connected_arr[now]:
            if visited[next_node] > time + next_time:
                visited[next_node] = time + next_time
                queue.append(next_node)

    return visited


n, m, x = map(int, input().split())
connections = [tuple(map(int, input().split())) for _ in range(m)]
connected = [[] for _ in range(n + 1)]
reverse_connected = [[] for _ in range(n + 1)]
for a, b, c in connections:
    connected[a].append((b, c))
    reverse_connected[b].append((a, c))  # 단방향이므로, 반대(각 노드들에서 x로 가는 걸, 다익스트라로 해결해주기 위해 반대 방향도 따로 저장)

first = dijkstra(x, connected)  # x에서 각 노드들로 가는 최단거리 배열
second = dijkstra(x, reverse_connected)  # 각 노드들에서 x로 가는 최단거리 배열

mx = 0
for i in range(1, n + 1):
    mx = max(mx, first[i] + second[i])  # 최대값 갱신
print(mx)


# 다익스트라 템플릿 정돈
"""
from heapq import heappop, heappush

def dijkstra(start, connected_arr):  # 다익스트라; 최단 경로 찾기
    visited = [1e9] * (n + 1)  # start에서 각 노드들로의 최단 거리 저장할 배열
    visited[start] = 0
    queue = [(0, start)]

    while queue:
        time, now = heappop(queue)

        if visited[now] < time:
            continue

        for next_node, next_time in connected_arr[now]:
            if visited[next_node] > time + next_time:
                visited[next_node] = time + next_time
                heappush(queue, (time + next_time, next_node))

    return visited


n, m, x = map(int, input().split())
connections = [tuple(map(int, input().split())) for _ in range(m)]
connected = [[] for _ in range(n + 1)]
reverse_connected = [[] for _ in range(n + 1)]
for a, b, c in connections:
    connected[a].append((b, c))
    reverse_connected[b].append((a, c))  # 단방향이므로, 반대(각 노드들에서 x로 가는 걸, 다익스트라로 해결해주기 위해 반대 방향도 따로 저장)

first = dijkstra(x, connected)  # x에서 각 노드들로 가는 최단거리 배열
second = dijkstra(x, reverse_connected)  # 각 노드들에서 x로 가는 최단거리 배열

mx = 0
for i in range(1, n + 1):
    mx = max(mx, first[i] + second[i])  # 최대값 갱신
print(mx)
"""