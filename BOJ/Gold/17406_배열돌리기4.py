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
