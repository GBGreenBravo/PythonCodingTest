# 20241127
# 41:05
# 1 / 5

# 로직은 틀리지 않았으나, deque말고 list로 bfs 구현해야 시간초과 안 나는 문제.

N, M, K = map(int, input().split())
area = [[int(aa) for aa in str(input())] for _ in range(N)]

visited = [[[N * M * 2] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 0

queue = [(0, 0, 0)]

answer = N * M * 2
time = 0
while queue:
    next_queue = []

    for y, x, broke_cnt in queue:
        if time % 2:  # 밤일때
            next_queue.append((y, x, broke_cnt))
            for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ny, nx = y + dy, x + dx
                if ny < 0 or N <= ny or nx < 0 or M <= nx:
                    continue
                if not area[ny][nx] and visited[ny][nx][broke_cnt] > time + 1:
                    visited[ny][nx][broke_cnt] = time + 1
                    next_queue.append((ny, nx, broke_cnt))

        else:  # 낮일때
            for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ny, nx = y + dy, x + dx
                if ny < 0 or N <= ny or nx < 0 or M <= nx:
                    continue
                if area[ny][nx] and broke_cnt != K and visited[ny][nx][broke_cnt + 1] > time + 1:
                    visited[ny][nx][broke_cnt + 1] = time + 1
                    next_queue.append((ny, nx, broke_cnt + 1))
                elif not area[ny][nx] and visited[ny][nx][broke_cnt] > time + 1:
                    visited[ny][nx][broke_cnt] = time + 1
                    next_queue.append((ny, nx, broke_cnt))

    if min(visited[-1][-1]) != N * M * 2:
        break
    queue = next_queue
    time += 1
else:
    answer = -2
answer = min(answer, min(visited[-1][-1]))
print(answer + 1)
print(*visited, sep="\n")
