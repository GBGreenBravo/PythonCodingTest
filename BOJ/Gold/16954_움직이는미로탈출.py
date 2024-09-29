# 20240929
# 15:02
# 1 / 2

# 제자리 반영 안 해서 틀렸음.

direction = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(yy, xx):
    return yy < 0 or 8 <= yy or xx < 0 or 8 <= xx


def bfs():
    global area

    visited = [[0] * 8 for _ in range(8)]
    visited[-1][0] = 1

    queue = [(7, 0)]

    while queue and not visited[0][-1]:

        next_queue = []
        while queue:
            y, x = queue.pop()
            if area[y][x]:
                continue

            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[ny][nx]:
                    continue

                if ny == 0 and nx == 7:
                    return 1

                next_queue.append((ny, nx))
                visited[ny][nx] = 1

        queue = next_queue
        area = [[0] * 8] + area[:-1]


area = [list(str(input())) for _ in range(8)]
for i in range(8):
    for j in range(8):
        area[i][j] = int(area[i][j] == '#')

print(bfs() or 0)
