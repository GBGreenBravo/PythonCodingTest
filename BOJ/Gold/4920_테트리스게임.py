# 20240805
# 14:24
# 1 / 1

block1 = ((0, 0), (0, 1), (0, 2), (0, 3))
block2 = ((0, 0), (0, 1), (1, 1), (1, 2))
block3 = ((0, 0), (0, 1), (0, 2), (1, 2))
block4 = ((0, 0), (0, 1), (0, 2), (1, 1))
block5 = ((0, 0), (0, 1), (1, 0), (1, 1))


def rotate(array):
    return [list(row[::-1]) for row in zip(*array)]


def oob(y, x):
    return not(0 <= y < n) or not(0 <= x < n)


def get_max(array, blocks):
    global mx
    for block in blocks:
        for y in range(n):
            for x in range(n):
                sm = 0
                for dy, dx in block:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx):
                        break
                    sm += array[ny][nx]
                else:
                    mx = max(mx, sm)


test_case_cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr_0 = [list(map(int, input().split())) for _ in range(n)]
    arr_90 = rotate(arr_0)
    arr_180 = rotate(arr_90)
    arr_270 = rotate(arr_180)

    mx = -4_000_000
    get_max(arr_0, [block1, block2, block3, block4, block5])
    get_max(arr_90, [block1, block2, block3, block4])
    get_max(arr_180, [block3, block4])
    get_max(arr_270, [block3, block4])

    print(f"{test_case_cnt}. {mx}")
    test_case_cnt += 1
