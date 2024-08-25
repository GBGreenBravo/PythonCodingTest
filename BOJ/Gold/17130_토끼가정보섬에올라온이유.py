# 20240825
# 20:39
# 1 / 3

from collections import deque

direction = ((-1, 1), (0, 1), (1, 1))  # 오른쪽으로만 이동


def oob(yy, xx):
    return yy < 0 or n <= yy or m <= xx  # 오른쪽으로만 이동하기에, xx < 0은 불필요


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]
carrot_cnts = []

for i in range(n):
    for j in range(m):
        if area[i][j] == 'R':
            sy, sx = i, j  # 초기 토끼 좌표
            break
    else:
        continue
    break

queue = deque()
queue.append((sy, sx, 0))

visited = [[-1] * m for _ in range(n)]  # 0으로 초기화 해서 틀렸었음. (시작 시 0개 들고 있기 때문에, 음수로 초기화 필요)
visited[sy][sx] = 0

while queue:
    y, x, now_carrot = queue.popleft()

    if area[y][x] == 'O':  # 쪽문이라면, 지금 가진 당근 개수 저장
        carrot_cnts.append(now_carrot)

    if now_carrot < visited[y][x]:  # 불필요한 연산 하지 않음
        continue

    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or area[ny][nx] == '#':  # 영역 밖 or 장애물
            continue
        if now_carrot + int(area[ny][nx] == 'C') <= visited[ny][nx]:  # 이전 방문 시, 가졌던 당근 개수 이하라면
            continue
        visited[ny][nx] = now_carrot + int(area[ny][nx] == 'C')  # 해당 좌표로의 당근 개수 최대값 갱신
        queue.append((ny, nx, now_carrot + int(area[ny][nx] == 'C')))

if carrot_cnts:
    print(max(carrot_cnts))
else:
    print(-1)
