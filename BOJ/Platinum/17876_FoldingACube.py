# 20241203
# 28:12
# 1 / 2

"""
      5
    3 1 2 6
      4
"""
ewns = (None,
        (2, 4, 3, 5),
        (6, 4, 1, 5),
        (1, 4, 6, 5),
        (2, 6, 3, 1),
        (2, 1, 3, 6),
        (3, 4, 2, 5))
direction = ((0, 1), (1, 0), (0, -1), (-1, 0))


def oob(y, x):
    return y < 0 or 6 <= y or x < 0 or 6 <= x


def check(sy, sx):
    visited = [[0] * 6 for _ in range(6)]
    visited[sy][sx] = 1
    queue = [(sy, sx, 1)]
    while queue:
        y, x, num = queue.pop(0)
        near = []
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] == '.':
                near.append((ny, nx, -1))
            elif visited[ny][nx]:
                near.append((ny, nx, visited[ny][nx]))
            else:
                near.append([ny, nx, 0])

        if num == 1:
            for dd in range(4):
                if not near[dd][-1]:
                    visited[near[dd][0]][near[dd][1]] = ewns[num][dd]
                    queue.append((near[dd][0], near[dd][1], ewns[num][dd]))
            continue

        for _ in range(4):
            for d in range(4):
                if ewns[num][d] == near[d][-1]:
                    for dd in range(4):
                        if not near[dd][-1]:
                            visited[near[dd][0]][near[dd][1]] = ewns[num][dd]
                            queue.append((near[dd][0], near[dd][1], ewns[num][dd]))
                    break
            else:
                near.append(near.pop(0))
                continue
            break

    v = [1] + [0] * 6
    for y in range(6):
        for x in range(6):
            v[visited[y][x]] = 1
    return all(v)


area = [str(input()) for _ in range(6)]
for i in range(5):
    for j in range(6):
        if area[i][j] == '#':
            print("can" if check(i, j) else "cannot", "fold")
            break
    else:
        continue
    break
