# 20240816
# 09:56
# 1 / 1

from heapq import heappush, heappop

n, m = map(int, input().split())
visible = list(map(int, input().split()))
visible[-1] = 0  # 최종 도착점에 도달할 수 있도록 invisible 처리
connections = [tuple(map(int, input().split())) for _ in range(m)]
connected = [[] for _ in range(n)]
for a, b, c in connections:
    connected[a].append((b, c))
    connected[b].append((a, c))

INF = n * 1e5
visited = [INF] * n  # 불가능한 최대값으로 초기화
visited[0] = 0

queue = [(0, 0)]  # cost, node
while queue:
    now_cost, now_node = heappop(queue)

    if now_node == n - 1:  # 도착지점이라면 break
        print(now_cost)
        break

    if now_cost > visited[now_node]:  # 갱신된 node로, 이미 계산된 node라면
        continue

    for next_node, next_cost in connected[now_node]:
        if visible[next_node]:  # 보이는 노드라면 continue
            continue
        if visited[next_node] > now_cost + next_cost:  # 기존 방문 비용보다, 지금 방문하려는 비용이 더 적다면
            visited[next_node] = now_cost + next_cost
            heappush(queue, (now_cost + next_cost, next_node))  # 비용 적은 순으로 꺼내도록, 넣을 때 비용을 앞의 인덱스에
else:  # 도착지점에 닿지 않고 queue 다 소모되면, -1 출력
    print(-1)
