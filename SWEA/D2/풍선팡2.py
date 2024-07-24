# 20240724
# 06:29
def count_flower_powder(array, x, y):
    len_x = len(array)
    len_y = len(array[0])
    dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
    flower_powder = array[x][y]
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or len_x <= nx or ny < 0 or len_y <= ny:
            continue
        else:
            flower_powder += array[nx][ny]
    return flower_powder


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    mx = -1
    for i in range(n):
        for j in range(m):
            mx = max(mx, count_flower_powder(board, i, j))

    print(f"#{test_case} {mx}")
