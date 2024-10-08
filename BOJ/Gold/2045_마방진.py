# 20201008
# 20:45
# 1 / 1

"""
0 1 6
3 0 7
4 9 0
"""
# 테케에서 주어지지 않은, 위와 같은 케이스를 생각해주는 것이 요구됐음.


def oob(y, x):
    return y < 0 or 3 <= y or x < 0 or 3 <= x


def find_criteria():
    for c_row in area:
        if 0 not in c_row:
            return sum(c_row)

    for col in range(3):
        for c_row in range(3):
            if not area[c_row][col]:
                break
        else:
            return area[0][col] + area[1][col] + area[2][col]

    if area[0][0] and area[1][1] and area[2][2]:
        return area[0][0] + area[1][1] + area[2][2]

    if area[0][2] and area[1][1] and area[2][0]:
        return area[0][2] + area[1][1] + area[2][0]

    return None


def check(sy, sx):
    rl = [0, 0]
    for dy, dx in (0, 1), (0, -1),:
        ny, nx = sy + dy, sx + dx
        while not oob(ny, nx) and area[ny][nx]:
            rl[0] += 1
            rl[1] += area[ny][nx]
            ny, nx = ny + dy, nx + dx
    if rl[0] == 2:
        return rl[1]

    ud = [0, 0]
    for dy, dx in (1, 0), (-1, 0),:
        ny, nx = sy + dy, sx + dx
        while not oob(ny, nx) and area[ny][nx]:
            ud[0] += 1
            ud[1] += area[ny][nx]
            ny, nx = ny + dy, nx + dx
    if ud[0] == 2:
        return ud[1]

    tl = [0, 0]
    for dy, dx in (1, 1), (-1, -1),:
        ny, nx = sy + dy, sx + dx
        while not oob(ny, nx) and area[ny][nx]:
            tl[0] += 1
            tl[1] += area[ny][nx]
            ny, nx = ny + dy, nx + dx
    if tl[0] == 2:
        return tl[1]

    tr = [0, 0]
    for dy, dx in (-1, 1), (1, -1),:
        ny, nx = sy + dy, sx + dx
        while not oob(ny, nx) and area[ny][nx]:
            tr[0] += 1
            tr[1] += area[ny][nx]
            ny, nx = ny + dy, nx + dx
    if tr[0] == 2:
        return tr[1]


area = [list(map(int, input().split())) for _ in range(3)]

criteria = find_criteria()
if criteria:
    while sum(map(lambda l_row: l_row.count(0), area)):
        for i in range(3):
            for j in range(3):
                if not area[i][j]:
                    if check(i, j):
                        area[i][j] = criteria - check(i, j)
else:
    """
    나 + 다 == 가빼고 계산
    가 + 다 == 나배고 계산
    가 + 나 == 다빼고 계산 

    가빼고 계산 + 나 빼고 계산 + 다 빼고 계산  == (가+나+다) * 2
    """
    empties = []
    except_for_empties = []
    for i in range(3):
        for j in range(3):
            if not area[i][j]:
                empties.append((i, j))
                except_for_empties.append(check(i, j))
    for i in range(3):
        ey, ex = empties[i]
        area[ey][ex] = sum(except_for_empties) // 2 - except_for_empties[i]

for row in area:
    print(*row)
