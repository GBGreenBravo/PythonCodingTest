# 20241225
# 1:55:41
# 1 / 4

"""
행이나 열이 1이라면:
    1이 하나라도 존재하면 => "0"
    다 0이면 => "1"

행과 열이 2 이상이라면:
    시작좌표나 도착좌표가 막혀있다면 => "0"
    (북/동 에서 이어진 장애물은 2로 표시 & 남/서 에서 이어된 장애물은 3으로 표시)
    BFS로 닿는지 체크. 안 닿으면 => "0"
    갈 수 있는 빈칸들 중, 주변8방향에 2나 3의 장애물이 있는 곳이면 => "1"
    위 다 안되면 "2"
"""

from collections import deque

direction_4 = ((0, 1), (0, -1), (1, 0), (-1, 0))
direction_8 = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))


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
