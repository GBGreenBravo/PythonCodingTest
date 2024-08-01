# 20240801
# 18:36
# 1 / 2

from collections import deque


def bfs():
    queue = deque()
    queue.append(home)

    while queue:
        y, x = queue.popleft()

        if abs(rock[0] - y) + abs(rock[1] - x) <= 1000:
            return True

        for i in range(n):
            if visited_conv[i] == 1:
                continue
            ny, nx = conv[i]
            if abs(ny - y) + abs(nx - x) <= 1000:
                visited_conv[i] = 1
                queue.append((ny, nx))

    return False


t = int(input())
for _ in range(t):
    n = int(input())
    home = tuple(map(int, input().split()))
    conv = [tuple(map(int, input().split())) for _ in range(n)]
    visited_conv = [0] * n
    rock = tuple(map(int, input().split()))

    print("happy" if bfs() else "sad")
