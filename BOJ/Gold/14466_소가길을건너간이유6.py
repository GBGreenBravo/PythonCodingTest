# 20240915
# 35:24
# 1 / 2

from collections import deque


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def bfs(sy, sx):
    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx))

    cow_cnt = 1

    while queue:
        y, x = queue.popleft()
        for ny, nx in connected[y][x]:
            if visited[ny][nx]:
                continue
            visited[ny][nx] = 1
            cow_cnt += area[ny][nx]
            queue.append((ny, nx))

    return k - cow_cnt  # 입력 좌표의 소가 길 건너지 않으면 만나지 못하는 소의 수 반환


n, k, r = map(int, input().split())

# 연결리스트 구현
connected = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(r):  # 인접리스트에 입력되는 길 저장
    a, b, c, d = map(lambda yx: int(yx) - 1, input().split())
    connected[a][b].append((c, d))
    connected[c][d].append((a, b))
for i in range(n):
    for j in range(n):
        # 현재좌표의 인접리스트를, 길로 연결되지 않은 인접좌표만 저장되도록 갱신
        new_connected = []
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0),):
            ni, nj = i + di, j + dj
            if oob(ni, nj):
                continue
            if (ni, nj) in connected[i][j]:
                continue
            new_connected.append((ni, nj))
        connected[i][j] = new_connected

# 소 정보 저장
area = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(lambda yx: int(yx) - 1, input().split())
    area[a][b] = 1

# 정답 출력
answer = 0
for i in range(n):
    for j in range(n):
        if area[i][j]:  # 소가 있다면
            answer += bfs(i, j)  # 길 안 건너면 못 만나는 소의 수 추가
print(answer // 2)
