# 20240924
# 13:14
# 1 / 2

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


# (sy, sx)의 BFS 그룹에 대해 모두 group_flag를 표시하고, 그룹의 수를 저장하는 함수
def count_group_cnt(sy, sx):
    group_cnt = 1  # 현재 그룹의 수

    group_visited[sy][sx] = group_flag  # 방문배열에 group_flag로 표시

    queue = deque()
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or group_visited[ny][nx] or walls[ny][nx]:
                continue
            group_visited[ny][nx] = group_flag  # 방문배열에 group_flag로 표시
            queue.append((ny, nx))
            group_cnt += 1

    group_cnts.append(group_cnt)  # 그룹의 수 추가 (index: group_flag)


n, m = map(int, input().split())

# 입력받는 벽 배열
walls = [list(str(input())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        walls[i][j] = int(walls[i][j])


group_cnts = [0]  # 각 그룹의 수를 표시
group_flag = 0
group_visited = [[0] * m for _ in range(n)]  # 칸별 각 그룹의 group_flag가 표시되는 배열
for i in range(n):
    for j in range(m):
        if not walls[i][j] and not group_visited[i][j]:  # 벽이 아니고 방문 안 했다면 -> 새 그룹 BFS 탐색
            group_flag += 1
            count_group_cnt(i, j)

# 벽 부쉈을 때, 이동가능한 칸 갱신
for i in range(n):
    for j in range(m):
        # 벽이라면
        if walls[i][j]:
            merged_groups = set()  # 인접한 칸에 같은 그룹이 있을 수 있기에, set()으로 관리

            for di, dj in direction:
                ni, nj = i + di, j + dj
                if oob(ni, nj) or walls[ni][nj]:
                    continue
                # 인접 칸이 빈칸이라면, 그룹번호(index) 추가
                merged_groups.add(group_visited[ni][nj])

            # 인접 그룹의 총합 + 1(현재 벽 좌표)를 10으로 나눈 나머지
            walls[i][j] = (sum([group_cnts[group] for group in merged_groups]) + 1) % 10

for row in walls:
    print(*row, sep="")


# 20240826
# 15:04
# 1 / 2

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def cal_bfs_for_zero_area(sy, sx):
    queue = deque()
    queue.append((sy, sx))

    bfs_record[sy][sx] = 1  # 현재 BFS에서 중복방문 방지를 위해 임의로 1 넣어둠

    indexes = [(sy, sx)]  # 이 함수의 0인접영역의 모든 좌표를 담을 배열

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] or bfs_record[ny][nx]:  # 영역 밖 / 0이 아님 / 중복방문 방지
                continue
            bfs_record[ny][nx] = 1  # 현재 BFS에서 중복방문 방지를 위해 임의로 1 넣어둠
            indexes.append((ny, nx))
            queue.append((ny, nx))

    area_value = len(indexes), sy, sx  # 이 0인접영역의 모든 좌표에 담아둘 튜플 (영역 넓이, bfs 시작 좌표)
    for iy, ix in indexes:
        bfs_record[iy][ix] = area_value


n, m = map(int, input().split())
area = [[int(i) for i in list(str(input()))] for _ in range(n)]
bfs_record = [[0] * m for _ in range(n)]  # 해당 인접 0영역의 넓이와 bfs()를 시작한 좌표를 담기 위한 배열
for i in range(n):
    for j in range(m):
        if not area[i][j] and not bfs_record[i][j]:  # 0이고 계산되지 않은 0의 좌표라면
            cal_bfs_for_zero_area(i, j)

answer = [[0] * m for _ in range(n)]  # 정답 출력을 위한 배열

for i in range(n):
    for j in range(m):
        if area[i][j]:
            near = set()  # 상하좌우의 어떤 영역들이 같은 영역에 해당될 수도 있으므로, set 활용
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if oob(ni, nj) or area[ni][nj]:
                    continue
                near.add(bfs_record[ni][nj])
            answer[i][j] = (sum(map(lambda x: x[0], near)) + 1) % 10  # (벽 허물었을 때 합쳐지는 영역들의 넓이 합 + 1) % 10

for row in answer:
    print(*row, sep="")
