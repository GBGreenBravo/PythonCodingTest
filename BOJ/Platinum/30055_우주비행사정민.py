# 20241126
# 1:10:42
# 1 / 4

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def make_next_areas():
    i, j, d = 0, 1, 1
    next_area1[0][0] = (0, 1)
    while not (i == N1 - 1 and j == 0):
        if j == M1 - 1 and d == 1:
            next_area1[i][j] = (i + 1, j)
            i += 1
            d = -1
        elif j == 0 and d == -1:
            next_area1[i][j] = (i + 1, j)
            i += 1
            d = 1
        else:
            next_area1[i][j] = (i, j + d)
            j += d
    next_area1[-1][0] = (0, 0)

    i, j, d = 0, 1, 1
    next_area2[0][0] = (0, 1)
    while not (i == N2 - 1 and j == 0):
        if j == M2 - 1 and d == 1:
            next_area2[i][j] = (i + 1, j)
            i += 1
            d = -1
        elif j == 0 and d == -1:
            next_area2[i][j] = (i + 1, j)
            i += 1
            d = 1
        else:
            next_area2[i][j] = (i, j + d)
            j += d
    next_area2[-1][0] = (0, 0)


def spread_black_holes():
    global black_holes

    next_black_holes = []
    for area_num, y, x in black_holes:
        if area_num == 1:
            ny, nx = next_area1[y][x]
            if area1[ny][nx] == 1:
                continue
            area1[ny][nx] = 1
            next_black_holes.append((1, ny, nx))
        else:
            ny, nx = next_area2[y][x]
            if area2[ny][nx] == 1:
                continue
            area2[ny][nx] = 1
            next_black_holes.append((2, ny, nx))
    black_holes = next_black_holes


def oob1(y, x):
    return y < 0 or N1 <= y or x < 0 or M1 <= x


def oob2(y, x):
    return y < 0 or N2 <= y or x < 0 or M2 <= x


def bfs():
    visited1 = [[0] * M1 for _ in range(N1)]
    visited1[0][0] = 1
    visited2 = [[0] * M2 for _ in range(N2)]
    queue = []
    queue.append((1, 0, 0, 0))  # areaNum, y, x, left_time(이동중)

    time = 0
    while queue:  # next_queue써서, time이 +1 될 때마다 반복 1회하는 BFS
        next_queue = []
        for area_num, y, x, left_time in queue:
            # 이동게이트 이동중이라면
            if left_time:
                next_queue.append((area_num, y, x, left_time - 1))  # 이동게이트 이동시간 -1 해서 추가
                if left_time == 1:  # 다음 턴에 이동게이트 나온다면 방문처리
                    if area_num == 1:
                        visited1[y][x] = 1
                    else:
                        visited2[y][x] = 1
                continue

            # 1번 차원인 경우
            if area_num == 1:
                if area1[y][x] == 1:  # 블랙홀(1)에 덮였다면 continue
                    continue
                if area1[y][x] == 2:  # 이동게이트 있다면
                    ny, nx = connected1[(y, x)]
                    if not visited2[ny][nx]:  # 연결된 2번차원의 좌표에 아직 방문 안 했다면 -> queue에 담기
                        next_queue.append((2, ny, nx, 2))  # 지금으로부터 3초 뒤에 방문하기에 다음 queue에서 꺼낼 거 생각해서 left_time은 2로 설정
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob1(ny, nx) or visited1[ny][nx] or area1[ny][nx] == 1:
                        continue
                    visited1[ny][nx] = 1
                    next_queue.append((1, ny, nx, 0))

            # 2번 차원인 경우
            else:
                if area2[y][x] == 1:  # 블랙홀(1)에 덮였다면 continue
                    continue
                if y == N2 - 1 and x == M2 - 1:  # 우주선 위치에 도달했다면, 도착시간 출력 & return
                    print(time)
                    return
                if area2[y][x] == 2:  # 이동게이트 있다면
                    ny, nx = connected2[(y, x)]
                    if not visited1[ny][nx]:
                        next_queue.append((1, ny, nx, 2))
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob2(ny, nx) or visited2[ny][nx] or area2[ny][nx] == 1:
                        continue
                    visited2[ny][nx] = 1
                    next_queue.append((2, ny, nx, 0))

        # 퍼지고 있는 블랙홀들 1칸씩 이동
        spread_black_holes()

        if next_queue:
            queue = next_queue
            time += 1
        else:
            break
    print("hing...")


K, N1, M1, N2, M2 = map(int, input().split())
area1 = [[0] * M1 for _ in range(N1)]
area2 = [[0] * M2 for _ in range(N2)]
A, B = map(int, input().split())
R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())

# 이동게이트 이동좌표 저장
connected1 = dict()
connected2 = dict()
for i in range(A):
    for j in range(B):
        area1[R1 + i][C1 + j] = 2
        area2[R2 + i][C2 + j] = 2
        connected1[(R1 + i, C1 + j)] = (R2 + i, C2 + j)
        connected2[(R2 + i, C2 + j)] = (R1 + i, C1 + j)

black_holes = []
for _ in range(K):
    dd, dr, dc = map(int, input().split())
    if dd == 1:
        area1[dr][dc] = 1
    else:  # elif dd == 2:
        area2[dr][dc] = 1
    black_holes.append((dd, dr, dc))

# 칸별로 블랙홀이 이동하는 다음 칸 좌표 저장 (룩업테이블 만들기)
next_area1 = [[None] * M1 for _ in range(N1)]
next_area2 = [[None] * M2 for _ in range(N2)]
make_next_areas()

# BFS
bfs()
