# 20241203
# 24:42
# 1 / 1

from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def bfs():
    visited = [[-1] * M for _ in range(N)]
    visited[sy][sx] = 0
    queue = deque()
    queue.append((sy, sx))
    while queue:
        y, x = queue.popleft()
        distance = visited[y][x]

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] != -1 or area[ny][nx]:
                continue
            visited[ny][nx] = distance + 1
            queue.append((ny, nx))
    return visited


def find_d(y, x):
    if y == 0 and x != M - 1:
        return 0
    if x == M - 1 and y != N - 1:
        return 1
    if y == N - 1 and x != 0:
        return 2
    if x == 0 and y != 0:
        return 3
    else:
        print("Not Here!")


def find_answer():
    min_answer = -1

    d = find_d(ey, ex)
    dy, dx = direction[d]
    by, bx = ey + dy, ex + dx
    time = 1

    while (by, bx) != (ey, ex):
        if a_visited[by][bx] != -1:
            a_arrival = a_visited[by][bx]
            if time % 2 == a_arrival % 2:
                now_answer = time
                while a_arrival > now_answer:
                    now_answer += (N - 1) * 2 + (M - 1) * 2
                if min_answer == -1:
                    min_answer = now_answer
                else:
                    min_answer = min(min_answer, now_answer)

        d = find_d(by, bx)
        dy, dx = direction[d]
        by, bx = by + dy, bx + dx
        time += 1

    return min_answer


N, M = map(int, input().split())
area = [list(str(input())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if area[i][j] == 'A':
            area[i][j] = 0
            sy, sx = i, j
        elif area[i][j] == 'B':
            area[i][j] = 0
            ey, ex = i, j
        else:
            area[i][j] = int(area[i][j] == 'G')

a_visited = bfs()
print(find_answer())
