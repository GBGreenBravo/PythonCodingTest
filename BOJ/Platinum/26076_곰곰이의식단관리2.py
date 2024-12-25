# 20241225
# 1:55:41
# 1 / 4

from collections import deque

direction_4 = ((0, 1), (0, -1), (1, 0), (-1, 0))
direction_8 = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))


def check():
    visited = [[0] * (M + 2) for _ in range(N + 2)]
    visited[1][1] = 1
    dq = deque([(1, 1)])
    while dq:
        y, x = dq.popleft()
        for dy, dx in direction_4:
            ny, nx = y + dy, x + dx
            if visited[ny][nx] or area[ny][nx]:
                continue
            if ny == N and nx == M:
                return False
            visited[ny][nx] = 1
            dq.append((ny, nx))
    return True


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

if N == 1 or M == 1:
    print(0 if sum(map(sum, area)) else 1)
else:
    if (area[0][1] and area[1][0]) or (area[-1][-2] and area[-2][-1]):
        print(0)
        exit()

    area = [[2] * (M + 2)] + [[3] + row + [2] for row in area] + [[3] * (M + 2)]
    for c in range(1, M + 1):
        if area[1][c] == 1:
            area[1][c] = 2
            oq = deque([(1, c)])
            while oq:
                ci, cj = oq.popleft()
                for di, dj in direction_8:
                    ni, nj = ci + di, cj + dj
                    if area[ni][nj] == 1:
                        area[ni][nj] = 2
                        oq.append((ni, nj))
        if area[N][c] == 1:
            area[N][c] = 3
            oq = deque([(N, c)])
            while oq:
                ci, cj = oq.popleft()
                for di, dj in direction_8:
                    ni, nj = ci + di, cj + dj
                    if area[ni][nj] == 1:
                        area[ni][nj] = 3
                        oq.append((ni, nj))
    for r in range(1, N):
        if area[r][M] == 1:
            area[r][M] = 2
            oq = deque([(r, M)])
            while oq:
                ci, cj = oq.popleft()
                for di, dj in direction_8:
                    ni, nj = ci + di, cj + dj
                    if area[ni][nj] == 1:
                        area[ni][nj] = 2
                        oq.append((ni, nj))
        if area[r][1] == 1:
            area[r][1] = 3
            oq = deque([(r, 1)])
            while oq:
                ci, cj = oq.popleft()
                for di, dj in direction_8:
                    ni, nj = ci + di, cj + dj
                    if area[ni][nj] == 1:
                        area[ni][nj] = 3
                        oq.append((ni, nj))

    start_visited = [[0] * (M + 2) for _ in range(N + 2)]
    start_visited[1][1] = 1
    sq = deque([(1, 1)])
    while sq:
        ci, cj = sq.popleft()
        for di, dj in direction_4:
            ni, nj = ci + di, cj + dj
            if start_visited[ni][nj] or area[ni][nj]:
                continue
            start_visited[ni][nj] = 1
            sq.append((ni, nj))
    if not start_visited[N][M]:
        print(0)
    else:
        if area[1][2] or area[2][1] or area[-2][-3] or area[-3][-2]:
            print(1)
            exit()

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if not start_visited[i][j] or (i, j) == (1, 1) or (i, j) == (N, M):
                    continue
                near = [0] * 8
                for d_idx, (di, dj) in enumerate(direction_8):
                    ni, nj = i + di, j + dj
                    if area[ni][nj]:
                        near[d_idx] = area[ni][nj]
                if 2 not in near or 3 not in near:
                    continue
                print(1)
                break
            else:
                continue
            break
        else:
            print(2)
