# 20241001
# 34:36
# 1 / 1

# 17143_낚시왕

"""
풀이 시간: 35분 (15:01 - 15:36)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:01 - 15:06)
    이전에 이 문제를 풀며 틀린 부분이 있어서, 디버깅을 꽤 했었는데,
    문제에서 주어진 1 2 3 4 방향을 0 1 2 3 으로 코드에서 바꿔줬고
    그로 인해 디버깅에서 헷갈린 부분이 많았습니다.

    그래서 그때를 기점으로,
    주어진 방향의 입력에 대해서 1 2 3 4와 같이 들어오면
    0 index에 None을 두는 식으로,
    디버깅/문제 친화적인 구현을 하기로 했습니다.


2. 구현 (15:06 - 15:26)
    이전에 실수했던 지점을 다시 실수할 수는 없었습니다.

    한 가지 달랐던 점은,
    이전 풀이에서는 벽에 닿는 좌표뿐만 아니라, 그 벽까지의 거리도 다 계산을 해줬는데,
    이번 풀이에서는 벽에 닿는 좌표만 체크하고 벽을 넘는 좌표를 꺾어주며 계산했습니다.


3. 디버깅 (15:26 - 15:35)
    복사 붙여넣기 과정에서 미처 변경해주지 못한 부분이 있었습니다.
    (direction[s_d_idx][1]를 direction[s_d_idx][0]로 적은 실수)
    복붙 과정에서 더 꼼꼼히 코드 하나하나 체크해줘야 함을 회고했습니다.

    그래도 해당 디버깅을 통해,
    (디버그 모드를 활용한) 체계적인 디버깅 절차를 점검할 수 있었습니다.
"""

direction = (None, (-1, 0), (1, 0), (0, 1), (0, -1))
opposite = [None, 2, 1, 4, 3]


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def all_mold_move():
    global area

    new_area = [[[] for _ in range(m)] for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if area[y][x]:
                s_dist, s_d_idx, s_size = area[y][x]
                if s_d_idx <= 2:
                    modified_dist = s_dist % (n * 2 - 2)

                    dy = direction[s_d_idx][0]

                    first_end = n - 1 if dy == 1 else 0
                    second_end = 0 if dy == 1 else n - 1

                    ny = y + dy * modified_dist
                    if not oob(ny, x):
                        new_area[ny][x].append((s_dist, s_d_idx, s_size))
                        continue

                    ny = first_end - (ny - first_end)
                    if not oob(ny, x):
                        new_area[ny][x].append((s_dist, opposite[s_d_idx], s_size))
                        continue

                    ny = second_end - (ny - second_end)
                    new_area[ny][x].append((s_dist, s_d_idx, s_size))

                else:
                    modified_dist = s_dist % (m * 2 - 2)

                    dx = direction[s_d_idx][1]

                    first_end = m - 1 if dx == 1 else 0
                    second_end = 0 if dx == 1 else m - 1

                    nx = x + dx * modified_dist
                    if not oob(y, nx):
                        new_area[y][nx].append((s_dist, s_d_idx, s_size))
                        continue

                    nx = first_end - (nx - first_end)
                    if not oob(y, nx):
                        new_area[y][nx].append((s_dist, opposite[s_d_idx], s_size))
                        continue

                    nx = second_end - (nx - second_end)
                    new_area[y][nx].append((s_dist, s_d_idx, s_size))

    for y in range(n):
        for x in range(m):
            if not new_area[y][x]:
                new_area[y][x] = 0
            elif len(new_area[y][x]) == 1:
                new_area[y][x] = new_area[y][x][0]
            else:
                new_area[y][x] = max(new_area[y][x], key=lambda nar: nar[2])
    area = new_area


n, m, k = map(int, input().split())
area = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    xx, yy, ss, dd, bb = map(int, input().split())
    area[xx - 1][yy - 1] = (ss, dd, bb)

answer = 0
for start_col in range(m):

    moving_row = 0
    while moving_row < n:
        if area[moving_row][start_col]:
            answer += area[moving_row][start_col][-1]
            area[moving_row][start_col] = []
            break
        moving_row += 1

    all_mold_move()
print(answer)
