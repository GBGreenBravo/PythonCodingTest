# 20240807
# 08:49
# 1 / 1

from collections import deque


def bfs(start_node):
    distance_sm = 0

    visited = [False] * n
    visited[start_node] = True
    queue = deque()
    queue.append((start_node, 0))

    while queue:
        now_node, distance = queue.popleft()  # 현재의 노드, 시작한 노드로부터의 거리
        distance_sm += distance

        for next_node in connected[now_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, distance + 1))

    global answer
    if distance_sm < answer[1]:  # 최소값이라면 갱신
        answer = (start_node + 1, distance_sm)


n, m = map(int, input().split())
connected = [[] for _ in range(n)]  # 양방향 간선을 저장하는 리스트
for _ in range(m):
    a, b = map(int, input().split())
    connected[a - 1].append(b - 1)
    connected[b - 1].append(a - 1)

answer = (-1, 10_000)  # 정답이될 node번호, 임의의 최소값
for i in range(n):  # 오름차순으로 node의 BFS 계산
    bfs(i)
print(answer[0])
