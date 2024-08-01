# 20240801
# 24:39
# 1 / 3

from collections import deque


def oob(y, x):
    return not(0 <= y < n) or not(0 <= x < m)


def bfs():
    queue = deque()
    queue.append((0, 0, 0))  # y, x, time

    visited = dict()
    visited[(0, 0)] = 1

    while queue:
        y, x, time = queue.popleft()

        if time > time_limit:  # 시간제한 넘어서면
            return False

        if y == n - 1 and x == m - 1:  # 공주를 찾았다면
            return time

        if castle[y][x] == 2:  # 그람을 찾았다면
            answer = time + abs(n - 1 - y) + abs(m - 1 - x)  # answer을 그대로 return 하면 안됨. 그람 찾아서 가는게 더 돌아갈 수도 있기 때문.
            global sword
            sword = False if answer > time_limit else answer

        time += 1
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited.get((ny, nx)) == 1 or castle[ny][nx] == 1:
                continue
            visited[(ny, nx)] = 1
            queue.append((ny, nx, time))

    return False


n, m, time_limit = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]
sword = False  # 이 값이나 bfs()의 반환값이나 False 말고 임의의 최대값으로 설정하면 더 간편할 듯.
result = bfs()
if sword:
    result = min(result, sword) if result else sword
print("Fail" if not result else result)
