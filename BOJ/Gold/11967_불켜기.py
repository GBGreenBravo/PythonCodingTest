# 20240929
# 35:46
# 1 / 3

# 방문한 칸 수가 아닌, (방문하지 않았어도) 불 킬 수 있는 방 수를 출력하는 문제였음.
# possibles에 중복된 좌표가 담길 수도 있음을 생각하지 못해, 또 틀림..

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or n <= xx


n, m = map(int, input().split())
connected = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    aa, bb, cc, dd = map(int, input().split())
    connected[aa - 1][bb - 1].append((cc - 1, dd - 1))

visited = [[0] * n for _ in range(n)]
visited[0][0] = 1

queue = []
queue.append((0, 0))

possibles = []

while queue:
    for y, x in queue:
        for ny, nx in connected[y][x]:
            if not visited[ny][nx]:
                possibles.append((ny, nx))

    next_possibles = []
    next_queue = []
    for y, x in possibles:
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or not visited[ny][nx]:
                continue
            break
        else:
            next_possibles.append((y, x))
            continue
        visited[y][x] = 1
        next_queue.append((y, x))

    possibles = next_possibles
    queue = next_queue

print(sum(map(sum, visited)) + len(set(possibles)))


# next_possibles/next_queue에 중복된 좌표 안 담기도록 리팩토링
"""
direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or n <= xx


n, m = map(int, input().split())
connected = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    aa, bb, cc, dd = map(int, input().split())
    connected[aa - 1][bb - 1].append((cc - 1, dd - 1))

visited = [[0] * n for _ in range(n)]
visited[0][0] = 1

queue = []
queue.append((0, 0))

possibles = []

while queue:
    for y, x in queue:
        for ny, nx in connected[y][x]:
            if not visited[ny][nx]:
                possibles.append((ny, nx))

    next_possibles = []
    next_queue = []
    for y, x in possibles:
        if visited[y][x]:
            continue
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or not visited[ny][nx]:
                continue
            visited[y][x] = 1
            next_queue.append((y, x))
            break
        else:
            next_possibles.append((y, x))
            continue


    possibles = next_possibles
    queue = next_queue

print(sum(map(sum, visited)) + len(set(possibles)))
"""