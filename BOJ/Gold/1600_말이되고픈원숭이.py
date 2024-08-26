# 20240826
# 09:40
# 1 / 1

from collections import deque

horse_direction = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2))  # 말 이동방향
monkey_direction = ((0, 1), (0, -1), (1, 0), (-1, 0))  # 원숭이 이동방향


def oob(yy, xx):
    return yy < 0 or h <= yy or xx < 0 or w <= xx


k = int(input())
w, h = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(h)]

visited = [[[0] * w for _ in range(h)] for _ in range(k + 1)]  # index번 말 이동 썼을 때의 방문배열
visited[0][0][0] = 1  # 0번 말 이동 쓴 시작 좌표 방문 처리

queue = deque([(0, 0, 0)])
while queue:
    y, x, used_k = queue.popleft()
    distance = visited[used_k][y][x]  # 이전까지의 거리를 불러오기

    if y == h - 1 and x == w - 1:  # 도착 지점 도착하면 print & break
        print(distance - 1)
        break

    for dy, dx in monkey_direction:  # 말 이동 소진 여부와는 관계 없이, 원숭이 이동
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or area[ny][nx] or visited[used_k][ny][nx]:
            continue
        visited[used_k][ny][nx] = distance + 1
        queue.append((ny, nx, used_k))

    if used_k == k:  # 말 이동 다 썼다면, 말 이동 못함
        continue

    for dy, dx in horse_direction:  # 말 이동
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or area[ny][nx] or visited[used_k + 1][ny][nx]:  # 현재 used_k에서 한번 더 말 이동 쓰므로, 한번 더 이동한 방문배열 활용
            continue
        visited[used_k + 1][ny][nx] = distance + 1
        queue.append((ny, nx, used_k + 1))

else:
    print(-1)


# 20240801
# 15:05
# 1 / 1

from collections import deque

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

monkey_move = ((0, 1), (0, -1), (1, 0), (-1, 0))
horse_move = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))

visited = [[[0] * w for _ in range(h)] for _ in range(k + 1)]

queue = deque()
queue.append((0, 0, 0))  # y, x, used_k
visited[0][0][0] = 1


def oob(yy, xx):
    return not(0 <= yy < h) or not(0 <= xx < w)


while queue:
    y, x, used_k = queue.popleft()
    distance = visited[used_k][y][x] + 1

    for dy, dx in monkey_move:
        ny, nx = y + dy, x + dx
        if not oob(ny, nx) and arr[ny][nx] != 1 and not visited[used_k][ny][nx]:
            visited[used_k][ny][nx] = distance
            queue.append((ny, nx, used_k))

    if used_k == k:
        continue
    used_k += 1
    for dy, dx in horse_move:
        ny, nx = y + dy, x + dx
        if not oob(ny, nx) and arr[ny][nx] != 1 and not visited[used_k][ny][nx]:
            visited[used_k][ny][nx] = distance
            queue.append((ny, nx, used_k))


answers = [visit[h - 1][w - 1] for visit in visited if visit[h - 1][w - 1] != 0]
print(min(answers) - 1 if answers else -1)


# answers에 저장할 필요 없이, BFS이기 때문에 거리순으로 탐색하므로, 마지막 좌표 만나면 return 시키면 됨.
"""
from collections import deque

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

monkey_move = ((0, 1), (0, -1), (1, 0), (-1, 0))
horse_move = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))

visited = [[[0] * w for _ in range(h)] for _ in range(k + 1)]

queue = deque()
queue.append((0, 0, 0))  # y, x, used_k
visited[0][0][0] = 1


def oob(yy, xx):
    return not(0 <= yy < h) or not(0 <= xx < w)


def bfs():
    while queue:
        y, x, used_k = queue.popleft()
        if y == h - 1 and x == w - 1:
            return visited[used_k][y][x] - 1

        distance = visited[used_k][y][x] + 1

        for dy, dx in monkey_move:
            ny, nx = y + dy, x + dx
            if not oob(ny, nx) and arr[ny][nx] != 1 and not visited[used_k][ny][nx]:
                visited[used_k][ny][nx] = distance
                queue.append((ny, nx, used_k))

        if used_k == k:
            continue
        used_k += 1
        for dy, dx in horse_move:
            ny, nx = y + dy, x + dx
            if not oob(ny, nx) and arr[ny][nx] != 1 and not visited[used_k][ny][nx]:
                visited[used_k][ny][nx] = distance
                queue.append((ny, nx, used_k))
    return -1


print(bfs())
"""