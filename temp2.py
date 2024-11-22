from collections import deque

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))


def oob(y, x):
    return y < 0 or M <= y or x < 0 or N <= x


def check_route_and_move(person_idx):
    global first_getter, getter_cnt

    sy, sx = people_arr[person_idx]

    visited = [[0] * N for _ in range(M)]
    visited[sy][sx] = 1

    queue = deque()
    for d_idx, (dy, dx) in enumerate(direction):
        ny, nx = sy + dy, sx + dx
        if not oob(ny, nx) and area[ny][nx] != 1:
            visited[ny][nx] = 1
            queue.append((ny, nx, d_idx))

    while queue:
        y, x, d = queue.popleft()
        if area[y][x] == 2:
            dy, dx = direction[d]
            ny, nx = sy + dy, sx + dx
            if area[ny][nx] == 2:
                if first_getter == -1:
                    first_getter = person_idx
                getter_cnt += 1
                moving[person_idx] = False
            else:
                people_arr[person_idx] = [ny, nx]
                people_area[sy][sx] = 0
            return True

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == 1:
                continue
            visited[ny][nx] = 1
            queue.append((ny, nx, d))

    return False


def bomb_attack(sy, sx):
    distance = 1
    done = [False] * 4

    while not sum(done):
        candidates = []

        for d, (dy, dx) in enumerate(direction):
            if done[d]:
                continue

            ny, nx = sy + dy * distance, sx + dx * distance
            if oob(ny, nx) or area[ny][nx] == 1:
                done[d] = True
                continue

            if people_area[ny][nx]:
                candidates.append((people_area[ny][nx], ny, nx))

        if candidates:
            p_idx, py, px = max(candidates)

            area[py][px] = 1
            temporary_walls.append([(py, px), C + 1])

            people_area[py][px] = 0
            moving[p_idx] = False
            return

        distance += 1


def reduce_temporary_walls():
    global temporary_walls

    next_walls = []
    for (wy, wx), duration in temporary_walls:
        duration -= 1
        if not duration:
            area[wy][wx] = 0
        else:
            next_walls.append(((wy, wx), duration))
    temporary_walls = next_walls


M, N, K, C = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(M)]

people_arr = [(None, None)] + [list(map(lambda inp: int(inp) - 1, input().split())) for _ in range(K)]
people_area = [[0] * M for _ in range(N)]
for idx, (pi, pj) in enumerate(people_arr):
    if not idx:
        continue
    people_area[pi][pj] = idx
moving = [False] + [True] * K

temporary_walls = []

first_getter = -1
getter_cnt = 0
turn = 0

while sum(moving):
    turn += 1
    for i in range(1, K + 1):
        if not moving[i]:
            continue

        if check_route_and_move(i):
            pi, pj = people_arr[i]
            another = people_area[pi][pj]
            if another:
                area[pi][pj] = 1
                temporary_walls.append([(pi, pj), C + 1])

                people_area[pi][pj] = 0
                moving[i], moving[another] = False, False
                continue
            else:
                people_area[pi][pj] = 1
                bomb_attack(pi, pj)

    reduce_temporary_walls()

print(first_getter)
print(getter_cnt)
print(turn)
