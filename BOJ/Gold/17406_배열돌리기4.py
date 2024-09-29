# 20240929
# 23:39
# 1 / 1

# 이전 풀이와 로직은 같지만, 룩업테이블 만들어놓고 활용한 게 차이.

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

rotating_indexes = [None]
for i in range(1, 25):
    now_indexes = []

    ry, rx = 0, 0
    for dy, dx in direction:
        for _ in range(i * 2):
            ry, rx = ry + dy, rx + dx
            now_indexes.append((ry, rx))

    rotating_indexes.append(now_indexes)


def rotate_all(arr):
    for idx in dfs_arr:
        sy, sx, sd = rotation_infos[idx]
        sy, sx = sy - 1, sx - 1

        for d in range(1, sd + 1):
            sy, sx = sy - 1, sx - 1
            dydxs = rotating_indexes[d]
            start = arr[sy + 1][sx]
            for di in range(len(dydxs) - 2, -1, -1):
                dy, dx = dydxs[di]
                dby, dbx = dydxs[di - 1]
                arr[sy + dy][sx + dx] = arr[sy + dby][sx + dbx]
            arr[sy][sx] = start

    return arr


def dfs(cnt):
    global min_answer

    if cnt == k:
        result_arr = rotate_all([r[:] for r in area])
        min_answer = min(min_answer, min(map(sum, result_arr)))
        return

    for idx in range(k):
        if idx not in dfs_arr:
            dfs_arr.append(idx)
            dfs(cnt + 1)
            dfs_arr.pop()


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
rotation_infos = list(tuple(map(int, input().split())) for _ in range(k))

min_answer = 100 * n * m
dfs_arr = []
dfs(0)
print(min_answer)


# 20240920
# 28:21
# 1 / 1


def rotate(cy, cx, d, arr):
    for depth in range(1, d + 1):
        rotated = []
        for i in range(depth * 2):
            rotated.append((cy - 1 - depth, cx - 1 - depth + i))
        for i in range(depth * 2):
            rotated.append((cy - 1 - depth + i, cx - 1 + depth))
        for i in range(depth * 2):
            rotated.append((cy - 1 + depth, cx - 1 + depth - i))
        for i in range(depth * 2):
            rotated.append((cy - 1 + depth - i, cx - 1 - depth))

        start = arr[rotated[-1][0]][rotated[-1][1]]
        for i in range(len(rotated) - 1, 0, -1):
            arr[rotated[i][0]][rotated[i][1]] = arr[rotated[i - 1][0]][rotated[i - 1][1]]
        arr[rotated[0][0]][rotated[0][1]] = start

    return arr


def rotate_and_get_min_answer(rotation_arr):
    copied_area = [row[:] for row in area]
    for r, c, s in rotation_arr:
        copied_area = rotate(r, c, s, copied_area)

    global min_answer
    min_answer = min(min_answer, min(map(sum, copied_area)))


def dfs(cnt, rotation_arr):
    if cnt == k:
        rotate_and_get_min_answer(rotation_arr)
        return

    for idx in range(k):
        if not visited[idx]:
            visited[idx] = 1
            dfs(cnt + 1, rotation_arr + [rotations[idx]])
            visited[idx] = 0


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
rotations = [tuple(map(int, input().split())) for _ in range(k)]

min_answer = n * m * 100

visited = [0] * k
dfs(0, [])

print(min_answer)
