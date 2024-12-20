# 20241220
# 52:06
# 1 / 3

N, M = map(int, input().split())
floor_elevators = [None] + [[] for _ in range(N)]
elevator_connected = [[] for _ in range(M)]
for e_idx in range(M):
    aa, bb = map(int, input().split())
    x = aa
    while x <= N:
        floor_elevators[x].append(e_idx)
        elevator_connected[e_idx].append(x)
        x += bb
start, end = map(int, input().split())

floor_visited = [None] + [0] * N
floor_visited[start] = [0, None]
elevator_visited = [0] * M
queue = [(start, '')]
while queue and not floor_visited[end]:
    next_queue = []
    for now, route in queue:
        for elev in floor_elevators[now]:
            if elevator_visited[elev]:
                continue
            elevator_visited[elev] = 1
            for nex in elevator_connected[elev]:
                if floor_visited[nex]:
                    continue
                floor_visited[nex] = [floor_visited[now][0] + 1, route + ' ' + str(elev + 1)]
                next_queue.append((nex, route + ' ' + str(elev + 1)))

    queue = next_queue

if not floor_visited[end]:
    print(-1)
else:
    print(floor_visited[end][0])
    print(*floor_visited[end][1].split(), sep="\n")
