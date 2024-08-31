# 20240825
# 14:56
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def cal_safe_zones():  # 현재의 area에 대해, 바이러스를 퍼뜨리고 안전영역 최대값을 갱신하는 함수
    queue = deque(virus_start_points)  # 초기 바이러스 위치로부터 시작
    visited = [[0] * m for _ in range(n)]  # 빈칸이었지만 바이러스 퍼지게 된 곳을 표시하는, 방문 배열

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if not oob(ny, nx) and not area[ny][nx] and not visited[ny][nx]:  # (영역 안 and 빈칸 and 중복방문X) 라면
                visited[ny][nx] = 1  # 바이러스 퍼진 빈칸 체크
                queue.append((ny, nx))  # BFS 큐에 담기

    global mx_safe_zone
    # 3: 벽 세워진 3군데 / sum(map(sum, visited)): 빈칸이었지만, 바이러스 퍼진 곳들
    # 위의 합을 초기의 0의 개수들에서 빼주면, 현재 상태에서의 안전영역이 계산됨.
    mx_safe_zone = max(mx_safe_zone, first_zeros - 3 - sum(map(sum, visited)))


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

virus_start_points = []  # 벽 3개 설치하고 BFS 시작할 때마다, queue에 담을 좌표들
first_zeros = 0  # 초기 0의 개수 (3개의 벽과, BFS의 결과로 0의 칸에 바이러스 퍼진 좌표들 수를 모두 빼주면 => 그 BFS에서의 안전영역의 개수가 됨)
for i in range(n):
    for j in range(m):
        if area[i][j] == 2:
            virus_start_points.append((i, j))
        elif not area[i][j]:
            first_zeros += 1

mx_safe_zone = 0
for i in range(0, n * m - 2):  # 좌표를 (y * m + x)로 생각하고 반복문 3개를 활용하여, 벽 세울 3개의 좌표를 구함.
    if area[i // m][i % m]:  # 빈칸이 아니라면 continue
        continue
    for j in range(i + 1, n * m - 1):
        if area[j // m][j % m]:
            continue
        for k in range(j + 1, n * m):
            if area[k // m][k % m]:
                continue

            area[i // m][i % m], area[j // m][j % m], area[k // m][k % m] = 1, 1, 1  # 빈칸들 모두 벽으로
            cal_safe_zones()  # 바이러스 퍼뜨리고 안전영역 최대값 갱신
            area[i // m][i % m], area[j // m][j % m], area[k // m][k % m] = 0, 0, 0  # 빈칸으로 복구
print(mx_safe_zone)


# cal_safe_zones()에서 바이러스 퍼진 곳을, sum(map(sum, visited))로 계산하기보다, virus_cnt 변수를 하나 두고, while문에서 하나씩 더해주는 게 시간 효율적임.
"""
from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def cal_safe_zones():
    queue = deque(virus_start_points)
    visited = [[0] * m for _ in range(n)]
    virus_cnt = 0

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if not oob(ny, nx) and not area[ny][nx] and not visited[ny][nx]: 
                visited[ny][nx] = 1
                queue.append((ny, nx))
                virus_cnt += 1

    global mx_safe_zone
    # 3: 벽 세워진 3군데 / virus_cnt: 빈칸이었지만, 바이러스 퍼진 곳들
    # 위의 합을 초기의 0의 개수들에서 빼주면, 현재 상태에서의 안전영역이 계산됨.
    mx_safe_zone = max(mx_safe_zone, first_zeros - 3 - virus_cnt)


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

virus_start_points = []
first_zeros = 0 
for i in range(n):
    for j in range(m):
        if area[i][j] == 2:
            virus_start_points.append((i, j))
        elif not area[i][j]:
            first_zeros += 1

mx_safe_zone = 0
for i in range(0, n * m - 2):
    if area[i // m][i % m]:
        continue
    for j in range(i + 1, n * m - 1):
        if area[j // m][j % m]:
            continue
        for k in range(j + 1, n * m):
            if area[k // m][k % m]:
                continue

            area[i // m][i % m], area[j // m][j % m], area[k // m][k % m] = 1, 1, 1
            cal_safe_zones()
            area[i // m][i % m], area[j // m][j % m], area[k // m][k % m] = 0, 0, 0
print(mx_safe_zone)
"""