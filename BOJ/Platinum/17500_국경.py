# 20241227
# 56:42
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def check():
    animal_visited = [[0] * N for _ in range(N)]
    for sy in range(N):
        for sx in range(N):
            if area[sy][sx] != '.' and not animal_visited[sy][sx]:
                now_animal = area[sy][sx]
                animal_visited[sy][sx] = 1
                queue = deque()
                queue.append((sy, sx))
                while queue:
                    y, x = queue.popleft()
                    if area[y][x] not in ('.', now_animal):
                        return False
                    for d_idx, (dy, dx) in enumerate(direction):
                        ny, nx = y + dy, x + dx
                        if ny < 0 or N <= ny or nx < 0 or N <= nx or animal_visited[ny][nx]:
                            continue
                        if d_idx == 0:
                            if ((y, x + 1), (y + 1, x + 1)) in borders:
                                continue
                        elif d_idx == 1:
                            if ((y, x), (y + 1, x)) in borders:
                                continue
                        elif d_idx == 2:
                            if ((y + 1, x), (y + 1, x + 1)) in borders:
                                continue
                        elif d_idx == 3:
                            if ((y, x), (y, x + 1)) in borders:
                                continue
                        animal_visited[ny][nx] = 1
                        queue.append((ny, nx))

    return True


def dfs(y, x, route):
    global done

    if y == N and x == N:
        if check():
            done = borders
        return

    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if ny < 0 or N + 1 <= ny or nx < 0 or N + 1 <= nx or dfs_visited[ny][nx]:
            continue
        dfs_visited[ny][nx] = 1
        adding_border = (min(route[-1], (ny, nx)), max(route[-1], (ny, nx)))
        borders.add(adding_border)
        dfs(ny, nx, [r[:] for r in route] + [(ny, nx)])
        if done:
            return
        borders.remove(adding_border)
        dfs_visited[ny][nx] = 0


def print_area():
    p_area = [[' '] * (4 * (N + 1) - 1) for _ in range(2 * (N + 1) + 1)]

    for y in range(len(p_area)):
        p_area[y][0] = '#'
        p_area[y][-1] = '#'
    for x in range(len(p_area[0])):
        p_area[0][x] = '#'
        p_area[-1][x] = '#'

    for y in range(1, len(p_area), 2):
        for x in range(1, len(p_area[0]), 4):
            p_area[y][x] = '+'

    for y in range(2, 2 * N + 1, 2):
        for x in range(3, 4 * N + 1, 4):
            p_area[y][x] = area[(y - 2) // 2][(x - 3) // 4]

    for y in range(N):
        for x in range(N):
            cy, cx = 2 + y * 2, 3 + x * 4
            if ((y, x + 1), (y + 1, x + 1)) in borders:
                p_area[cy][cx + 2] = '|'
            if ((y, x), (y + 1, x)) in borders:
                p_area[cy][cx - 2] = '|'
            if ((y + 1, x), (y + 1, x + 1)) in borders:
                p_area[cy + 1][cx - 1], p_area[cy + 1][cx], p_area[cy + 1][cx + 1] = '-', '-', '-'
            if ((y, x), (y, x + 1)) in borders:
                p_area[cy - 1][cx - 1], p_area[cy - 1][cx], p_area[cy - 1][cx + 1] = '-', '-', '-'

    for p_row in p_area:
        print(*p_row, sep="")


N = int(input())
area = [list(str(input())) for _ in range(N)]
points = [[0] * (N + 1) for _ in range(N + 1)]
dfs_visited = [[0] * (N + 1) for _ in range(N + 1)]
dfs_visited[0][0] = 1
borders = set()
done = False
dfs(0, 0, [(0, 0)])

if not done:
    print("no")
else:
    print("yes")
    print_area()
