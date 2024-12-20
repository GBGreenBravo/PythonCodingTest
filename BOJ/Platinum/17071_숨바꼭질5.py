# 20241220
# 35:04
# 1 / 2


def s_bfs():
    s_visited = [[-1] * 2 for _ in range(500_001)]
    s_visited[N][0] = 0
    time = 0
    queue = [N]
    candidates = []
    while queue:
        next_queue = []
        for now in queue:
            if d_visited[now] != -1:
                if time % 2 == d_visited[now] % 2 and time <= d_visited[now]:
                    candidates.append(d_visited[now])

            for nex in (now - 1, now + 1, now * 2):
                if nex < 0 or 500_000 < nex or s_visited[nex][(time + 1) % 2] != -1:
                    continue
                s_visited[nex][(time + 1) % 2] = time + 1
                next_queue.append(nex)

        queue = next_queue
        time += 1

    print(min(candidates or [-1]))


def d_bfs():
    visited = [-1] * 500_001
    dist = 1
    d = K
    while not (d < 0 or 500_000 < d):
        visited[d] = dist - 1
        d += dist
        dist += 1
    return visited


N, K = map(int, input().split())
d_visited = d_bfs()
s_bfs()
