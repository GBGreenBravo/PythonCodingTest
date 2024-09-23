# 20240922
# 34:25
# 1 / 3

# 문제의 '만약 막힌 면이 바닥을 향할 때 도둑이 같은 칸에 있다면 도둑은 바로 승리를 선언하고 탐정은 패배하게 된다.'
# 지문을 반영해주지 않아서(continue 미작성) 2번 틀림.

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


# 정육면체 굴린 결과를 반환하는 함수
def roll(dice, direction_idx):
    down, up, east, west, north, south = dice

    if direction_idx == 0:
        return east, west, up, down, north, south
    elif direction_idx == 1:
        return west, east, down, up, north, south
    elif direction_idx == 2:
        return south, north, east, west, down, up
    elif direction_idx == 3:
        return north, south, east, west, up, down


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

# 초기 세팅 (갈 수 있는/없는 칸 구분(0/1) + 시작위치/종료위치 탐색)
for i in range(n):
    for j in range(m):
        if area[i][j] == '#':
            area[i][j] = 1
        elif area[i][j] == '.':
            area[i][j] = 0
        elif area[i][j] == 'D':
            sy, sx = i, j
            area[i][j] = 0
        elif area[i][j] == 'R':
            ey, ex = i, j
            area[i][j] = 0

# 감옥빈칸의 index(0-5)에 따라, 칸별로 [아래, 위, 동, 서, 북, 남]을 방문 배열로 선언.
visited = [[[0] * 6 for _ in range(m)] for _ in range(n)]
visited[sy][sx][0] = 1  # 시작 시, 아래에 감옥빈칸 있음.

# BFS
queue = deque()
queue.append((sy, sx, (1, 0, 0, 0, 0, 0)))

result_prison, result_distance = [], []  # 종료위치에서의 (감옥 상태 / 지나온 거리)를 담을 배열

while queue:
    y, x, prison = queue.popleft()
    distance = visited[y][x][prison.index(1)]

    for di in range(4):
        dy, dx = direction[di]
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or area[ny][nx]:
            continue

        # 다음의 감옥 상태 불러오기
        next_prison = roll(prison, di)
        prison_empty = next_prison.index(1)
        if visited[ny][nx][prison_empty]:  # 이미 방문했던 상태의 감옥이면 continue
            continue

        # 종료위치 -> 결과 저장 & continue(!!!)
        if ny == ey and nx == ex:
            result_prison.append(next_prison)
            result_distance.append(distance)
            continue

        visited[ny][nx][prison_empty] = distance + 1
        queue.append((ny, nx, roll(prison, di)))

# 결과 출력
if result_prison:
    for r_idx in range(len(result_prison)):
        if result_prison[r_idx][0]:
            print(result_distance[r_idx])
            break
    else:
        print(-1)
else:
    print(-1)
