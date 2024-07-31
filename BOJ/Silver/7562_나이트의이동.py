# 20240731
# 07:07

direction = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))


def oob(yy, xx):
    return not(0 <= yy < l) or not(0 <= xx < l)


t = int(input())
for _ in range(t):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    board[si][sj] = 1
    queue = [(si, sj)]
    while queue:
        y, x = queue.pop(0)
        if y == ei and x == ej:
            break
        cnt = board[y][x] + 1

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            if not board[ny][nx]:
                board[ny][nx] = cnt
                queue.append((ny, nx))

    print(board[ei][ej] - 1)


# 아래는 deque를 활용한 풀이
# deque 선언하면서 초기값 설정할 때는 list에 담아줘야 함.
"""
from collections import deque

direction = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))


def oob(yy, xx):
    return not(0 <= yy < l) or not(0 <= xx < l)


t = int(input())
for _ in range(t):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    board[si][sj] = 1
    # queue = deque((si, sj))
    queue = deque([(si, sj)])
    while queue:
        y, x = queue.popleft()
        if y == ei and x == ej:
            break
        cnt = board[y][x] + 1

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            if not board[ny][nx]:
                board[ny][nx] = cnt
                queue.append((ny, nx))

    print(board[ei][ej] - 1)
"""