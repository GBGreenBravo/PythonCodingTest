# 20240723
# 05:35

def count_abs(array, x, y):
    nn = len(array)
    dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)

    sm_count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nn <= nx or ny < 0 or nn <= ny:
            continue
        else:
            sm_count += abs(array[x][y] - array[nx][ny])
    return sm_count


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    sm = 0
    for i in range(n):
        for j in range(n):
            sm += count_abs(arr, i, j)
    print(f"#{test_case} {sm}")


# 아래와 같이 (dx,dy)코드 축약 가능.
"""
def count_abs(array, x, y):
    nn = len(array)
    sm_count = 0
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < nn and 0 <= ny < nn:
            sm_count += abs(array[x][y] - array[nx][ny])
    return sm_count


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    sm = 0
    for i in range(n):
        for j in range(n):
            sm += count_abs(arr, i, j)
    print(f"#{test_case} {sm}")
"""