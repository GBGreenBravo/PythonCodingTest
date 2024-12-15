# 20241215
# 1 / 1

N, K, M = map(int, input().split())
tubes = [list(map(int, input().split())) for _ in range(M)]
tube_infos = [None] + [[] for _ in range(N)]
for t_idx, tube in enumerate(tubes):
    for t in tube:
        tube_infos[t].append(t_idx)
answer = None
tube_visited = [0] * len(tubes)
visited = [1] * 2 + [0] * (N - 1)
queue = [1]
distance = 1
while queue:
    next_queue = []
    for now in queue:
        if now == N:
            answer = distance
        for t_idx in tube_infos[now]:
            if tube_visited[t_idx]:
                continue
            tube_visited[t_idx] = 1
            for nex in tubes[t_idx]:
                if not visited[nex]:
                    visited[nex] = 1
                    next_queue.append(nex)
    if answer:
        break
    queue = next_queue
    distance += 1
print(answer if answer else -1)
