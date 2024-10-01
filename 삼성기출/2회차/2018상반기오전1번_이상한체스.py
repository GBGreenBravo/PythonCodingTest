# 20240930
# 22:20
# 1 / 1

# 15683_감시

"""
풀이 시간: 22분 (15:14 - 15:36)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:14 - 15:18)


2. 구현 (15:18 - 15:31)
    이전 풀이에서는 함수화 & 2차원배열을 임의로 설정한 flag(7)로 바꾸며 방문처리
    했었습니다.
    이전 풀이도 괜찮으나, 현재 정착된 풀이 스타일로는 이번에 구현한 게 더 가까운 듯 합니다.


3. 디버깅 (15:31 - 15:34)
    area[cy][cx] == 2 가 아닌 area[cy][cx] 이 조건으로 적혀있던 단순 실수였습니다.
"""

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 동남서북


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def check(direction_arr):
    copied_visited = [vv[:] for vv in visited]
    for idx, (sy, sx) in enumerate(candidates):

        dy, dx = direction[direction_arr[idx]]
        y, x = sy + dy, sx + dx
        while not oob(y, x) and area[y][x] != 6:
            copied_visited[y][x] = 1
            y, x = y + dy, x + dx

        if area[sy][sx] in (3, 4):
            dy, dx = direction[(direction_arr[idx] + 1) % 4]
            y, x = sy + dy, sx + dx
            while not oob(y, x) and area[y][x] != 6:
                copied_visited[y][x] = 1
                y, x = y + dy, x + dx

        if area[sy][sx] in (2, 4):
            dy, dx = direction[(direction_arr[idx] + 2) % 4]
            y, x = sy + dy, sx + dx
            while not oob(y, x) and area[y][x] != 6:
                copied_visited[y][x] = 1
                y, x = y + dy, x + dx

    global min_answer
    min_answer = min(min_answer, n * m - sum(map(sum, copied_visited)))


def dfs(idx, direction_arr):
    if idx == len_candidates:
        check(direction_arr)
        return

    cy, cx = candidates[idx]
    if area[cy][cx] == 2:
        dfs(idx + 1, direction_arr + [0])
        dfs(idx + 1, direction_arr + [1])
    else:
        dfs(idx + 1, direction_arr + [0])
        dfs(idx + 1, direction_arr + [1])
        dfs(idx + 1, direction_arr + [2])
        dfs(idx + 1, direction_arr + [3])


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
candidates = []

for i in range(n):
    for j in range(m):
        if area[i][j]:
            visited[i][j] = 1

            if area[i][j] in (1, 2, 3, 4):
                candidates.append((i, j))

            elif area[i][j] == 5:
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    while not oob(ni, nj) and area[ni][nj] != 6:
                        visited[ni][nj] = 1
                        ni, nj = ni + di, nj + dj

len_candidates = len(candidates)
min_answer = n * m
dfs(0, [])
print(min_answer)
