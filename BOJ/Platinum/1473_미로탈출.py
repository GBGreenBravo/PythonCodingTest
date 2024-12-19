# 20241219
# 25:49
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def cal_next_status(string, row, col, d_idx):
    if string == 'A':
        return True
    elif string == 'B':
        return False
    elif string == 'C':
        if (not row and not col) or (row and col):
            return d_idx in (2, 3)
        else:
            return d_idx in (0, 1)
    else:
        if (not row and not col) or (row and col):
            return d_idx in (0, 1)
        else:
            return d_idx in (2, 3)


def bfs():
    visited = [[[[0] * 2**M for _ in range(2**N)] for _ in range(M)] for _ in range(N)]
    visited[0][0][0][0] = 1
    queue = deque()
    queue.append((0, 0, 0, False, 0, 0))
    while queue:
        y, x, time, clicked, row, col = queue.popleft()
        if y == N - 1 and x == M - 1:
            return time

        for d_idx, (dy, dx) in enumerate(direction):
            if not cal_next_status(area[y][x], row & 1 << y, col & 1 << x, d_idx):
                continue
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            if not cal_next_status(area[ny][nx], row & 1 << ny, col & 1 << nx, d_idx):
                continue
            if visited[ny][nx][row][col]:
                continue
            visited[ny][nx][row][col] = 1
            queue.append((ny, nx, time + 1, False, row, col))

        if not clicked:
            new_row = row - (1 << y) if row & (1 << y) else row + (1 << y)
            new_col = col - (1 << x) if col & (1 << x) else col + (1 << x)
            if not visited[y][x][new_row][new_col]:
                visited[y][x][new_row][new_col] = 1
                queue.append((y, x, time + 1, True, new_row, new_col))
    return -1


N, M = map(int, input().split())
area = [list(str(input())) for _ in range(N)]
print(bfs())
