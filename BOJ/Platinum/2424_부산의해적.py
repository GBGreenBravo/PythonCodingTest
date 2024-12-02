# 20241202
# 1:02:21
# 1 / 3

from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
opposite = (2, 3, 0, 1)


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def get_pirate_sight():
    visited = [[0] * M for _ in range(N)]
    visited[spy][spx] = 1
    direction_visited = [[[0] * 5 for _ in range(M)] for _ in range(N)]  # 0~4 : 방향별 방문처리 / 5 : 최소 방문 체크
    for idx in range(5):
        direction_visited[spy][spx][idx] = 1
    queue = deque()
    queue.append((spy, spx))
    while queue:
        y, x = queue.popleft()
        distance = visited[y][x]

        # 현재 칸에서 4방향 최소값 갱신
        for d_idx, (dy, dx) in enumerate(direction):
            cy, cx = y + dy, x + dx
            while not oob(cy, cx):
                if area[cy][cx] == 1:  # 섬이면 -> break
                    break
                d_v, o_d_v = direction_visited[cy][cx][d_idx], direction_visited[cy][cx][opposite[d_idx]]
                if (d_v and d_v < distance) or (o_d_v and o_d_v < distance):  # 이 방향과 반대방향 쌍(상하/좌우)에, 이미 더 작은 값 존재한다면 -> break
                    break
                direction_visited[cy][cx][d_idx] = distance  # 방향 최소값 갱신
                origin_value = direction_visited[cy][cx][-1]
                if not origin_value or origin_value > distance:  # 최소값 갱신
                    direction_visited[cy][cx][-1] = distance
                if area[cy][cx] == 2:  # 보물이면(바다는 아니기에) -> break
                    break
                cy, cx = cy + dy, cx + dx

        # 일반 BFS
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == 1:
                continue
            visited[ny][nx] = distance + 1
            queue.append((ny, nx))
            direction_visited[ny][nx][-1] = min(direction_visited[ny][nx][-1], distance + 1)  # 최소값 갱신

    # 방향별 방문체크 이제 필요없으니, 칸별 최소방문만 반환
    direction_visited = [[col[-1] for col in row] for row in direction_visited]
    return direction_visited


def solve():
    visited = [[0] * M for _ in range(N)]
    visited[ssy][ssx] = 1

    queue = deque()
    queue.append((ssy, ssx))

    while queue:
        y, x = queue.popleft()
        distance = visited[y][x]

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == 1:
                continue

            if pirate_sight[ny][nx] <= distance + 1:  # 해적 시선이 이 시점 이전으로 가능한 곳이면 -> continue
                continue

            if area[ny][nx] == 2:
                print("YES")
                return

            visited[ny][nx] = distance + 1
            queue.append((ny, nx))

    print("NO")


N, M = map(int, input().split())
area = [list(str(input())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if area[i][j] == '.':
            area[i][j] = 0
        elif area[i][j] == 'I':
            area[i][j] = 1
        elif area[i][j] == 'Y':
            ssy, ssx = i, j
            area[i][j] = 0
        elif area[i][j] == 'V':
            spy, spx = i, j
            area[i][j] = 0
        elif area[i][j] == 'T':
            area[i][j] = 2

# (해적 BFS) 해적이 이동해서 칸별로 못 들어가는 시점이 저장된 배열 가져오기
pirate_sight = get_pirate_sight()
# (수아 BFS) 가능한 곳 이동하고 "YES"/"NO" 출력
solve()
