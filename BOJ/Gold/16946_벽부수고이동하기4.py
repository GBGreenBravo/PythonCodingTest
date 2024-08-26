# 20240826
# 15:04
# 1 / 1

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
