# 20241205
# 36:23
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def find_up_left_and_indexes(sy, sx):
    area[sy][sx] = 0
    queue = deque([(sy, sx)])
    index_arr = [(sy, sx)]
    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or not area[ny][nx]:
                continue
            area[ny][nx] = 0
            queue.append((ny, nx))
            index_arr.append((ny, nx))

    up = min(a[0] for a in index_arr)
    left = min(a[1] for a in index_arr)

    return up, left, sorted([(a[0] - up, a[1] - left) for a in index_arr])


def find_shape(index_arr):
    for alpha_num, now_shapes in shapes.items():
        for now_shape in now_shapes:
            if index_arr == now_shape:
                return alpha_num

    return None


def save_shape(alpha_num, index_arr):
    h, w = max(a[0] for a in index_arr) + 1, max(a[1] for a in index_arr) + 1
    arr = [[0] * w for _ in range(h)]
    for iy, ix in index_arr:
        arr[iy][ix] = 1

    now_shapes = []

    now_shapes.append(sorted([(y, x) for x in range(len(arr[0])) for y in range(len(arr)) if arr[y][x]]))
    for d in range(3):
        arr = [list(r)[::-1] for r in zip(*arr)]
        now_shapes.append(sorted([(y, x) for x in range(len(arr[0])) for y in range(len(arr)) if arr[y][x]]))

    arr = arr[::-1]
    now_shapes.append(sorted([(y, x) for x in range(len(arr[0])) for y in range(len(arr)) if arr[y][x]]))
    for d in range(3):
        arr = [list(r)[::-1] for r in zip(*arr)]
        now_shapes.append(sorted([(y, x) for x in range(len(arr[0])) for y in range(len(arr)) if arr[y][x]]))

    shapes[alpha_num] = now_shapes


def carve(y, x, index_arr, alpha_num):
    for dy, dx in index_arr:
        area[y + dy][x + dx] = chr(alpha_num)


M = int(input())
N = int(input())
area = [[int(i) for i in str(input())] for _ in range(N)]

shapes = dict()

flag = ord('a') - 1
for i in range(N):
    for j in range(M):
        if area[i][j] == 1:
            u, l, indexes = find_up_left_and_indexes(i, j)
            s = find_shape(indexes)
            if not s:
                flag += 1
                save_shape(flag, indexes)
                s = flag
            carve(u, l, indexes, s)

for row in area:
    print(*row, sep="")
