# 20240731
# 15:11

n, m = map(int, input().split())
maze = [list(str(input())) for _ in range(n)]
possible = [[-1] * m for _ in range(n)]  # -1 : 탐색 전 , 0 : 불가능 , 1 : 가능


def find_path(y, x):
    now = y, x
    path = []
    path_dict = {}

    while True:
        path.append(now)
        path_dict[now] = 1
        if maze[now[0]][now[1]] == "U":
            ny, nx = now[0] - 1, now[1]
        elif maze[now[0]][now[1]] == "R":
            ny, nx = now[0], now[1] + 1
        elif maze[now[0]][now[1]] == "D":
            ny, nx = now[0] + 1, now[1]
        elif maze[now[0]][now[1]] == "L":
            ny, nx = now[0], now[1] - 1

        if not(0 <= ny < n) or not(0 <= nx < m):
            for py, px in path:
                possible[py][px] = 1
            break

        # 아래에서 갔던 경로 탐색을 (ny, nx) in path 조건으로 하게 되면, 시간복잡도가 500**2 * 500이 되므로, 갔던 경로 탐색을 O(1)만에 할 수 있어야 한다.
        if path_dict.get((ny, nx)) == 1:
            for py, px in path:
                possible[py][px] = 0
            break

        if possible[ny][nx] != -1:
            for py, px in path:
                possible[py][px] = possible[ny][nx]
            break

        now = ny, nx


for i in range(n):
    for j in range(m):
        if possible[i][j] == -1:
            find_path(i, j)

print(sum([sum(row) for row in possible]))


# dict 말고 path의 possible 좌표들을 -2와 같은 새로운 값으로 바꾸는 방법도 있다.
"""
n, m = map(int, input().split())
maze = [list(str(input())) for _ in range(n)]
possible = [[-1] * m for _ in range(n)]  # -1 : 탐색 전 , 0 : 불가능 , 1 : 가능 , -2 : 탐색 중


def find_path(y, x):
    now = y, x
    path = []

    while True:
        path.append(now)
        possible[now[0]][now[1]] = -2
        if maze[now[0]][now[1]] == "U":
            ny, nx = now[0] - 1, now[1]
        elif maze[now[0]][now[1]] == "R":
            ny, nx = now[0], now[1] + 1
        elif maze[now[0]][now[1]] == "D":
            ny, nx = now[0] + 1, now[1]
        elif maze[now[0]][now[1]] == "L":
            ny, nx = now[0], now[1] - 1

        if not(0 <= ny < n) or not(0 <= nx < m):
            for py, px in path:
                possible[py][px] = 1
            break

        if possible[ny][nx] == -2:
            for py, px in path:
                possible[py][px] = 0
            break

        if possible[ny][nx] != -1:
            for py, px in path:
                possible[py][px] = possible[ny][nx]
            break

        now = ny, nx


for i in range(n):
    for j in range(m):
        if possible[i][j] == -1:
            find_path(i, j)

print(sum([sum(row) for row in possible]))
"""