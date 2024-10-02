# 20241001
# 28:21
# 1 / 1

# 17144_미세먼지안녕

"""
풀이 시간: 28분 (14:31 - 14:59)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:31 - 14:35)


2. 구현 (14:35 - 14:59)
    청소되는 위/아래 루트가 하드코딩된 부분이 있어서, 체크포인트로 중간 검증하는 과정에서
    자잘한 실수들이 발견돼서 시간이 조금 더 소요됐습니다.

    이전 풀이와 청소루트를 찾는 코드에 차이가 있었습니다.
    이전에는 for문 4번으로 구현했다면,
    이번에는 visited 배열을 두어서 나선형 루트 탐색하는 것처럼 시계/반시계 방향으로 꺾으며 찾았습니다.

    그리고 enumerate의 활용도가 늘어가고 있다는 점에 의의가 있기도 합니다.


3. 디버깅 (-)
"""

direction = ((0, 1), (-1, 0), (0, -1), (1, 0))  # 동북서남


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def spread_dusts():
    added_dust = [[0] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if area[y][x] >= 5:
                spread_dust = area[y][x] // 5

                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or area[ny][nx] == -1:
                        continue
                    added_dust[ny][nx] += spread_dust
                    area[y][x] -= spread_dust

    for y in range(n):
        for x in range(m):
            if added_dust[y][x]:
                area[y][x] += added_dust[y][x]


def clean():
    for idx, (y, x) in enumerate(upper_indexes[:-1]):
        ny, nx = upper_indexes[idx + 1]
        area[y][x] = area[ny][nx]
    area[upper_indexes[-1][0]][upper_indexes[-1][1]] = 0

    for idx, (y, x) in enumerate(lower_indexes[:-1]):
        ny, nx = lower_indexes[idx + 1]
        area[y][x] = area[ny][nx]
    area[lower_indexes[-1][0]][lower_indexes[-1][1]] = 0


n, m, t = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 1):
    if area[i][0] == -1:
        upper, lower = i, i + 1
        break

visited = [[0] * m for _ in range(n)]

visited[upper][0] = 1
visited[lower][-1] = 1
upper_indexes = []
uy, ux, ud = upper - 1, 0, 1
while True:
    upper_indexes.append((uy, ux))
    duy, dux = direction[ud]
    nuy, nux = uy + duy, ux + dux
    if nuy == upper and nux == 0:
        break
    if oob(nuy, nux) or visited[nuy][nux]:
        ud = (ud - 1) % 4
        duy, dux = direction[ud]
        nuy, nux = uy + duy, ux + dux
    uy, ux = nuy, nux
    visited[uy][ux] = 1

visited[lower][-1] = 0
visited[lower][0] = 1
lower_indexes = []
ly, lx, ld = lower + 1, 0, 3
while True:
    lower_indexes.append((ly, lx))
    dly, dlx = direction[ld]
    nly, nlx = ly + dly, lx + dlx
    if nly == lower and nlx == 0:
        break
    if oob(nly, nlx) or visited[nly][nlx]:
        ld = (ld + 1) % 4
        dly, dlx = direction[ld]
        nly, nlx = ly + dly, lx + dlx
    ly, lx = nly, nlx

for _ in range(t):
    spread_dusts()
    clean()

print(sum(map(sum, area)) + 2)
