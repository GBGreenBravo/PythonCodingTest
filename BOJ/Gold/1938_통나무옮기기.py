# 20240812
# 53:57
# 1 / 1


from collections import deque

n = int(input())
area = [list(str(input())) for _ in range(n)]
first_B, center_B = None, None
first_E, center_E = None, None
for i in range(n):
    for j in range(n):
        if area[i][j] == 'B':
            if not first_B:
                first_B = (i, j)
            elif not center_B:
                center_B = (i, j)
            area[i][j] = '0'

        elif area[i][j] == 'E':
            if not first_E:
                first_E = (i, j)
            elif not center_E:
                center_E = (i, j)
            area[i][j] = '0'

B_vertical = 1 if first_B[0] != center_B[0] else 0
E_vertical = 1 if first_E[0] != center_E[0] else 0

visited = [[[False] * n for _ in range(n)] for _ in range(2)]  # 수평 / 수직
visited[B_vertical][center_B[0]][center_B[1]] = 1
queue = deque()
queue.append((center_B[0], center_B[1], B_vertical))


def oob(y, x):
    return (y < 0) or (n <= y) or (x < 0) or (n <= x)


vertical_direction = (((-1, 0), (-2, 0)), ((1, 0), (2, 0)), ((0, -1), (-1, -1), (1, -1)), ((0, 1), (-1, 1), (1, 1)))
horizontal_direction = (((-1, 0), (-1, -1), (-1, 1)), ((1, 0), (1, -1), (1, 1)), ((0, -1), (0, -2)), ((0, 1), (0, 2)))
turn_direction = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

possible = False
while queue:
    y, x, log_direction = queue.popleft()

    if (y, x) == center_E and log_direction == E_vertical:
        possible = True
        break

    if log_direction == 1:  # 수직 상하좌우
        for direction in vertical_direction:
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[ny][nx] == '1':
                    break
            else:
                dy, dx = direction[0]
                ny, nx = y + dy, x + dx
                if not visited[1][ny][nx]:
                    visited[1][ny][nx] = visited[1][y][x] + 1
                    queue.append((ny, nx, 1))
    else:  # 수평 상하좌우
        for direction in horizontal_direction:
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[ny][nx] == '1':
                    break
            else:
                dy, dx = direction[0]
                ny, nx = y + dy, x + dx
                if not visited[0][ny][nx]:
                    visited[0][ny][nx] = visited[0][y][x] + 1
                    queue.append((ny, nx, 0))

    # 회전
    for dy, dx in turn_direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or area[ny][nx] == '1':
            break
    else:
        if not visited[(log_direction + 1) % 2][y][x]:
            visited[(log_direction + 1) % 2][y][x] = visited[log_direction][y][x] + 1
            queue.append((y, x, (log_direction + 1) % 2))


if possible:
    print(visited[log_direction][y][x] - 1)
else:
    print(0)
