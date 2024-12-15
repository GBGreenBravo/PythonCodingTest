# 20241215
# 49:28
# 1 / 3

from heapq import heappop, heappush


def find_min_route():
    distances = [1e6] * N
    distances[0] = 0
    hq = [(0, 0)]
    while hq:
        dist, now = heappop(hq)
        if distances[now] != dist:
            continue
        if now == N - 1:
            break
        for nex, added in enumerate(connected[now]):
            if added and dist + added < distances[nex]:
                distances[nex] = dist + added
                heappush(hq, (dist + added, nex))

    routes = []
    q = [(N - 1, distances[-1])]
    v = [0] * N
    v[N - 1] = 1
    while q:
        now, dist = q.pop()
        for bef, subtracted in enumerate(connected[now]):
            if subtracted and not v[bef] and dist - subtracted == distances[bef]:
                routes.append((bef, now))
                q.append((bef, dist - subtracted))
                v[bef] = 1
    return routes


def dijkstra():
    distances = [1e6] * N
    distances[0] = 0
    hq = [(0, 0)]
    while hq:
        dist, now = heappop(hq)
        if distances[now] != dist:
            continue
        if now == N - 1:
            return dist
        for nex, added in enumerate(connected[now]):
            if added and dist + added < distances[nex]:
                distances[nex] = dist + added
                heappush(hq, (dist + added, nex))


N, M = map(int, input().split())
connected = [[0] * N for _ in range(N)]
for _ in range(M):
    xx, yy, zz = map(int, input().split())
    connected[xx - 1][yy - 1] = zz
    connected[yy - 1][xx - 1] = zz

max_answer = 0

candidates = find_min_route()
for x, y in candidates:
    tmp = connected[x][y]
    connected[x][y], connected[y][x] = 0, 0
    max_answer = max(max_answer, dijkstra())
    connected[x][y], connected[y][x] = tmp, tmp

print(max_answer)
