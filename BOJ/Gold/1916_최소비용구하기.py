# 20240816
# 06:21
# 1 / 1

from heapq import heappush, heappop

n = int(input())
m = int(input())
buses = [tuple(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())

connected = [[] for _ in range(n + 1)]
for a, b, c in buses:
    connected[a].append((b, c))

INF = int(1e10)
visited = [INF] * (n + 1)
visited[start] = 0

queue = [(0, start)]  # cost, city_number
while queue:
    cost_sum, city = heappop(queue)

    if city == end:  # 도착지점이라면 최소 비용 answer에 저장
        answer = cost_sum
        break

    if visited[city] < cost_sum:  # 이미 갱신된 노드라면 continue
        continue

    for next_city, next_cost in connected[city]:
        if visited[next_city] > cost_sum + next_cost:  # 다음 노드로 가는 경우가, 기존보다 더 적은 비용이라면
            visited[next_city] = cost_sum + next_cost
            heappush(queue, (cost_sum + next_cost, next_city))

print(answer)
