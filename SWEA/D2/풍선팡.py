# 20240724
# 16:20

def count_flower_powder(array, y, x, move):
    sm = move
    len_y, len_x = len(array), len(array[0])
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y, x
        for mv in range(1, move + 1):
            ny += dy
            nx += dx
            if 0 <= ny < len_y and 0 <= nx < len_x:
                sm += array[ny][nx]
    return sm


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(n)]
    mx = 0
    for i in range(n):
        for j in range(m):
            mx = max(mx, count_flower_powder(balloons, i, j, balloons[i][j]))
    print(f"#{test_case} {mx}")
