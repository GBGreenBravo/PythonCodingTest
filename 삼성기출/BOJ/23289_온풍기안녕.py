# 20240910 & 20240918
# 0 / 2    & 1 / 2
# 2:30:00  & 1:19:12

"""
풀이 시간: 1시간 19분 12초
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상


2. 구현


3. 검증


4. IndexError (16:38 - 17:07)
    바람 부는 칸 자체가 oob인 경우를 처리 못해줌..
"""

direction = (None, (0, 1), (0, -1), (-1, 0), (1, 0))  # X동서북남


def oob(y, x):
    return y < 0 or r <= y or x < 0 or c <= x


def wind_blows():
    for wy, wx, wd in wind_origins:
        dy, dx = direction[wd]
        wind_added = [[0] * c for _ in range(r)]
        wind_added[wy + dy][wx + dx] = 5
        for ww in range(4):
            wind_degree = 4 - ww
            range_r = range(wy + (2 + ww)*dy, wy + (2 + ww)*dy + 1*dy, dy) if dy else range(wy - (ww + 1), wy + (ww + 1) + 1)
            range_c = range(wx + (2 + ww)*dx, wx + (2 + ww)*dx + 1*dx, dx) if dx else range(wx - (ww + 1), wx + (ww + 1) + 1)
            for y in range_r:
                for x in range_c:
                    if oob(y, x):
                        continue

                    by, bx = y - dy, x - dx
                    if oob(by, bx) or str(by * c + bx) + " " + str(y * c + x) in walls:
                        continue
                    if wind_added[by][bx]:
                        wind_added[y][x] = wind_degree
                        continue

                    if dy:
                        others = ((y - dy, x - 1), (y - dy, x + 1))
                    else:
                        others = ((y - 1, x - dx), (y + 1, x - dx))

                    for oy, ox in others:
                        if oob(oy, ox) or not wind_added[oy][ox]:
                            continue
                        if str(oy * c + ox) + ' ' + str(by * c + bx) in walls:
                            continue
                        wind_added[y][x] = wind_degree
                        break

        for y in range(r):
            for x in range(c):
                if wind_added[y][x]:
                    area[y][x] += wind_added[y][x]


def moderate_temperature():
    changed_area = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            for dy, dx in direction[1:]:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[y][x] <= area[ny][nx] or str(y * c + x) + " " + str(ny * c + nx) in walls:
                    continue
                diff = (area[y][x] - area[ny][nx]) // 4
                if diff:
                    changed_area[y][x] += -diff
                    changed_area[ny][nx] += diff
    for y in range(r):
        for x in range(c):
            area[y][x] += changed_area[y][x]


def lower_edges():
    for i in range(1, r - 1):
        if area[i][0]:
            area[i][0] -= 1
        if area[i][c - 1]:
            area[i][c - 1] -= 1
    for i in range(c):
        if area[0][i]:
            area[0][i] -= 1
        if area[r - 1][i]:
            area[r - 1][i] -= 1


def investigate():
    for y, x in investigated:
        if area[y][x] < k:
            return False
    return True


r, c, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(r)]

w = int(input())
walls = set()
for _ in range(w):
    a, b, t = map(int, input().split())
    a, b = a - 1, b - 1
    if t:
        aa = a * c + b
        bb = a * c + b + 1
        walls.add(str(aa) + " " + str(bb))
        walls.add(str(bb) + " " + str(aa))
    else:
        aa = a * c + b
        bb = (a - 1) * c + b
        walls.add(str(aa) + " " + str(bb))
        walls.add(str(bb) + " " + str(aa))

wind_origins = []
investigated = []
for ii in range(r):
    for jj in range(c):
        if area[ii][jj] in [1, 2, 3, 4]:
            wind_origins.append((ii, jj, area[ii][jj]))
            area[ii][jj] = 0
        if area[ii][jj] == 5:
            area[ii][jj] = 0
            investigated.append((ii, jj))

chocolates = 0
while True:
    wind_blows()
    moderate_temperature()
    lower_edges()
    chocolates += 1
    if investigate() or chocolates > 100:
        break
print(chocolates)
