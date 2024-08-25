# 20240825
# 19:40
# 1 / 2

# 첫 풀이에서, 지훈이가 가는 곳에 대해서는 따로 방문 중복체크를 안 해줘서, 메모리 초과가 났었음.
# 이런 실수는 테케에서 잡히지 않을 가능성이 농후하므로, 정말 신경써줘야 함!

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or r <= yy or xx < 0 or c <= xx


def escape_from_fires_and_maze():
    queue = deque()
    for fire in fires:
        queue.append((*fire, True))  # 불이 퍼지기 시작할 좌표들
    queue.append((*jihun, False))  # 지훈이의 좌표

    jihun_visited = [[0] * c for _ in range(r)]
    jihun_visited[jihun[0]][jihun[1]] = 1

    while queue:
        y, x, is_fire = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                if is_fire:  # 불이 영역 밖으로 간다면, 그냥 continue
                    continue
                else:  # 지훈이가 영역 밖으로 간다면, 최단시간 반환
                    return jihun_visited[y][x]
            if area[ny][nx] == '#' or area[ny][nx] == 'F':
                continue
            if area[ny][nx] == '.':
                if is_fire:
                    area[ny][nx] = 'F'  # 불의 방문체크는 'F'로
                    queue.append((ny, nx, True))
                elif not jihun_visited[ny][nx]:
                    jihun_visited[ny][nx] = jihun_visited[y][x] + 1  # 지훈이의 방문 체크 필수!!
                    queue.append((ny, nx, False))

    return 'IMPOSSIBLE'


r, c = map(int, input().split())
area = [list(str(input())) for _ in range(r)]
fires = []
for i in range(r):
    for j in range(c):
        if area[i][j] == 'J':
            area[i][j] = '.'
            jihun = (i, j)
        elif area[i][j] == 'F':
            fires.append((i, j))

print(escape_from_fires_and_maze())
