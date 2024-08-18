# 20240818
# 1 / 5

from heapq import heappush, heappop

n, m = map(int, input().split())
connections = [(i, tuple(map(int, input().split()))) for i in range(m)]
connected = [[] for _ in range(n + 1)]
for idx, (a, b) in connections:
    connected[a].append((b, idx))
    connected[b].append((a, idx))

visited = [1e11] * (n + 1)
visited[1] = 0

queue = [(0, 1)]  # time, node

while queue:  # 다익스트라를 활용한 최단거리 찾기
    time, now_node = heappop(queue)
    now_idx = time % m

    if now_node == n:  # 종료 조건
        print(time)
        break

    if visited[now_node] < time:  # 이미 계산된 노드
        continue

    for next_node, next_idx in connected[now_node]:
        if next_idx >= now_idx:  # m주기에서 현재idx 이후에 다음idx이 위치한 경우
            next_time = time + (next_idx - now_idx) + 1  # +1은 횡단보도 이동 시간
        else:  # m주기에서 다음idx 뒤에 현재idx이 위치한 경우
            next_time = time + (m - now_idx) + next_idx + 1

        if visited[next_node] > next_time:
            visited[next_node] = next_time
            heappush(queue, (next_time, next_node))
