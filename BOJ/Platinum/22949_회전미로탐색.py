# 20241030
# 1:17:28
# 1 / 7

# 풀이 구상은 잘 했으나, 구현 과정에서 "이동or가만히 후 배열 회전" 디테일을 명확히 구현하지 못해 여러 번 틀렸던 문제.

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def same_group(y1, x1, y2, x2):
    return (y1 // 4 == y2 // 4) and (x1 // 4 == x2 // 4)


def rotate_index(y, x, remain_cnt):
    if remain_cnt in (0, 4):
        return y, x

    sy, sx = (y // 4) * 4, (x // 4) * 4
    cy, cx = sy + 1.5, sx + 1.5
    dy, dx = y - cy, x - cx
    ny, nx = int(cy + dx), int(cx - dy)
    return rotate_index(ny, nx, remain_cnt - 1)


def bfs():
    visited = [[[0] * 4 for _ in range(N)] for _ in range(N)]
    visited[si][sj][0] = 1

    queue = deque()
    queue.append((si, sj, 0, 0))
    queue.append((si, sj, 1, 1))

    while queue:
        y, x, rotated_cnt, distance = queue.popleft()

        if area[y][x] == 'E':
            return distance

        more_rotated_cnt = (rotated_cnt + 1) % 4

        if not visited[y][x][rotated_cnt]:
            queue.append((y, x, more_rotated_cnt, distance + 1))
            visited[y][x][rotated_cnt] = 1

        for dy, dx in direction:
            ry, rx = rotate_index(y, x, rotated_cnt)
            ny, nx = ry + dy, rx + dx
            if oob(ny, nx):
                continue
            if same_group(y, x, ny, nx):
                ny, nx = rotate_index(ny, nx, 4 - rotated_cnt)
                if not visited[ny][nx][rotated_cnt] and area[ny][nx] != '#':
                    queue.append((ny, nx, more_rotated_cnt, distance + 1))
                    visited[ny][nx][rotated_cnt] = 1
            else:  # elif not same_group(y, x, ny, nx):
                if not visited[ny][nx][0] and area[ny][nx] != '#':
                    queue.append((ny, nx, 1, distance + 1))
                    visited[ny][nx][0] = 1


K = int(input())
N = 4 * K
area = [list(str(input())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if area[i][j] == 'S':
            area[i][j] = '.'
            si, sj = i, j

result = bfs()
print(result if result else -1)
