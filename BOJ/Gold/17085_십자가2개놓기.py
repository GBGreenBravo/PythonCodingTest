# 20241010
# 17:53
# 1 / 1

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def find_max_length(sy, sx):
    max_length = n
    for dy, dx in direction:
        y, x = sy + dy, sx + dx
        now_length = 1
        while not oob(y, x) and area[y][x] == '#':
            now_length += 1
            y, x = y + dy, x + dx
        max_length = min(max_length, now_length - 1)
    return max_length


def check(y1, x1, len1, y2, x2, len2):
    visited = [[0] * m for _ in range(n)]
    visited[y1][x1] = 1
    for dy, dx in direction:
        for lll in range(1, len1 + 1):
            visited[y1 + dy * lll][x1 + dx * lll] = 1

    if visited[y2][x2]:
        return False
    visited[y2][x2] = 1
    for dy, dx in direction:
        for lll in range(1, len2 + 1):
            if visited[y2 + dy * lll][x2 + dx * lll]:
                return False
    return True


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

extent = [i * 4 + 1 for i in range(n)]

max_answer = 1

for i in range(n * m):
    iy, ix = divmod(i, m)
    if area[iy][ix] == '.':
        continue
    l1 = find_max_length(iy, ix)
    for j in range(i + 1, n * m):
        jy, jx = divmod(j, m)
        if area[jy][jx] == '.':
            continue
        l2 = find_max_length(jy, jx)

        if extent[l1] * extent[l2] <= max_answer:
            continue

        for ll1 in range(0, l1 + 1):
            for ll2 in range(0, l2 + 1):
                if extent[ll1] * extent[ll2] > max_answer:
                    if check(iy, ix, ll1, jy, jx, ll2):
                        max_answer = extent[ll1] * extent[ll2]

print(max_answer)
