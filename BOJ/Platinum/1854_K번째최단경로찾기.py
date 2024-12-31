# 20241230
# 18:03
# 1 / 1

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
connected = [None] + [[] for _ in range(N)]
for _ in range(M):
    aa, bb, cc = map(int, input().split())
    connected[aa].append((bb, cc))

visited = [None] + [[] for _ in range(N)]
visited[1].append(0)
queue = [(0, 1)]
while queue:
    cost, now = heappop(queue)

    for nex, added in connected[now]:
        next_cost = cost + added
        if len(visited[nex]) < K:
            heappush(visited[nex], -next_cost)
            heappush(queue, (cost + added, nex))
        else:
            if -next_cost > visited[nex][0]:
                heappop(visited[nex])
                heappush(visited[nex], -next_cost)
                heappush(queue, (cost + added, nex))

for node in range(1, N + 1):
    if len(visited[node]) < K:
        print(-1)
    else:
        print(-visited[node][-K])
