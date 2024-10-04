# 20240911
# 2:30:00 & 47:00
# 0 / 2   & 1 / 2

"""
풀이 시간: 47분 (23:08 ~ 23:55)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상


2. 구현


3. 검증


4. 틀렸습니다
    불필요한 중복방문 방지 처리를 해서 틀렸습니다.
    분명 문제 지문에는 없는 지시사항이었지만, DFS에서 습관적으로 쓴 코드로부터 비롯된 실수였습니다.
    그렇게 한번 잘못 쓰인 코드를 바탕으로 문제가 인지돼서, 찾기가 쉽지는 않았던 실수였습니다.
"""

direction_8 = ((1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0))
direction_4 = (None, (-1, 0), (0, -1), (1, 0), (0, 1))


def oob(y, x):
    return y < 0 or 4 <= y or x < 0 or 4 <= x


def move_fish(sy, sx, d_idx):
    for d in range(8):
        dy, dx = direction_8[d_idx - d]
        ny, nx = sy + dy, sx + dx
        if oob(ny, nx) or (shark_y == ny and shark_x == nx) or sum(fish_smell[ny][nx]):
            continue
        new_area[ny][nx].append((d_idx - d) % 8)
        return

    new_area[sy][sx].append(d_idx)
    return


def move_shark(cnt, y, x, fish_sum, d_string):
    if cnt == 3:
        shark_routes.append((fish_sum, d_string))
        return

    for d in range(1, 5):
        dy, dx = direction_4[d]
        ny, nx = y + dy, x + dx
        if not oob(ny, nx):
            shark_visited[y][x] = 1
            now_fish = len(new_area[ny][nx]) if not shark_visited[ny][nx] else 0
            if ny == shark_y and nx == shark_x:
                now_fish = len(new_area[ny][nx])
            move_shark(cnt + 1, ny, nx, fish_sum + now_fish, d_string + str(d))
            shark_visited[y][x] = 0


m, s = map(int, input().split())
fish_area = [[[] for _ in range(4)] for _ in range(4)]
fish_smell = [[[0, 0] for _ in range(4)] for _ in range(4)]
for _ in range(m):
    fffy, fffx, fffd = map(int, input().split())
    fish_area[fffy - 1][fffx - 1].append(fffd % 8)
shark_y, shark_x = map(int, input().split())
shark_y, shark_x = shark_y - 1, shark_x - 1

for _ in range(s):
    copied_area = [r[:] for r in fish_area]

    new_area = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for fd in fish_area[i][j]:
                move_fish(i, j, fd)

    shark_routes = []
    shark_visited = [[0] * 4 for _ in range(4)]
    move_shark(0, shark_y, shark_x, 0, '')

    selected = sorted(shark_routes, key=lambda info: (-info[0], info[1]))[0]

    deleted_indexes = []
    for i in range(3):
        dsy, dsx = direction_4[int(selected[1][i])]
        shark_y, shark_x = shark_y + dsy, shark_x + dsx
        if new_area[shark_y][shark_x]:
            deleted_indexes.append((shark_y, shark_x))
            new_area[shark_y][shark_x] = []

    for i in range(4):
        for j in range(4):
            fish_smell[i][j].append(1 if (i, j) in deleted_indexes else 0)
            fish_smell[i][j].pop(0)

    for i in range(4):
        for j in range(4):
            new_area[i][j].extend(copied_area[i][j])

    fish_area = new_area

answer = 0
for i in range(4):
    for j in range(4):
        answer += len(fish_area[i][j])
print(answer)
