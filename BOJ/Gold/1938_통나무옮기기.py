# 20240812
# 53:57
# 1 / 1


from collections import deque

n = int(input())
area = [list(str(input())) for _ in range(n)]
first_B, center_B = None, None  # 수평/수직 파악을 위해 2개만 있어도 됨.
first_E, center_E = None, None
for i in range(n):
    for j in range(n):
        if area[i][j] == 'B':
            if not first_B:
                first_B = (i, j)
            elif not center_B:
                center_B = (i, j)
            area[i][j] = '0'  # 원활한 탐색을 위해 0으로 변경

        elif area[i][j] == 'E':
            if not first_E:
                first_E = (i, j)
            elif not center_E:
                center_E = (i, j)
            area[i][j] = '0'

B_vertical = 1 if first_B[0] != center_B[0] else 0  # 수평은 0 수직은 1
E_vertical = 1 if first_E[0] != center_E[0] else 0

visited = [[[False] * n for _ in range(n)] for _ in range(2)]  # 0: 수평 visited / 1: 수직 visited
visited[B_vertical][center_B[0]][center_B[1]] = 1
queue = deque()
queue.append((center_B[0], center_B[1], B_vertical))  # 통나무 가운데 좌표와 방향을 기준으로 queue에 담기


def oob(y, x):
    return (y < 0) or (n <= y) or (x < 0) or (n <= x)


# 수직/수평 방향에 대해서는 각 요소의 0번째 인덱스에는 상하좌우에서 다음으로 갈 중심 좌표를 배치.
vertical_direction = (((-1, 0), (-2, 0)), ((1, 0), (2, 0)), ((0, -1), (-1, -1), (1, -1)), ((0, 1), (-1, 1), (1, 1)))
horizontal_direction = (((-1, 0), (-1, -1), (-1, 1)), ((1, 0), (1, -1), (1, 1)), ((0, -1), (0, -2)), ((0, 1), (0, 2)))
turn_direction = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

possible = False
while queue:
    y, x, log_direction = queue.popleft()

    if (y, x) == center_E and log_direction == E_vertical:  # 최종 목적지에 도착했다면 break
        possible = True
        break

    if log_direction == 1:  # 수직 상하좌우
        for direction in vertical_direction:
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[ny][nx] == '1':
                    break
            else:  # 이 방향으로 갈 수 있다면
                dy, dx = direction[0]
                ny, nx = y + dy, x + dx
                if not visited[1][ny][nx]:  # 다음 중심좌표를 수직 방문 안 했었다면
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
                if not visited[0][ny][nx]:  # 다음 중심좌표를 수평 방문 안 했었다면
                    visited[0][ny][nx] = visited[0][y][x] + 1
                    queue.append((ny, nx, 0))

    # 회전
    for dy, dx in turn_direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or area[ny][nx] == '1':
            break
    else:  # 회전을 위한 주변 좌표 이상 없다면
        if not visited[(log_direction + 1) % 2][y][x]:
            visited[(log_direction + 1) % 2][y][x] = visited[log_direction][y][x] + 1
            queue.append((y, x, (log_direction + 1) % 2))


if possible:
    print(visited[log_direction][y][x] - 1)  # 1부터 시작했기에, -1
else:
    print(0)
