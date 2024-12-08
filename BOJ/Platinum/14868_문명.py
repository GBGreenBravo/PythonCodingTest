# 20241208
# 59:59
# 1 / 6

# spread() BFS함수에서 nny,nnx 탐색할 생각 안 하고, check_spreading_near() 재사용해서
# & remain_civilizations를 int가 아닌 set()으로 관리해서, 시간초과가 났음.

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def check_spreading_near():
    global remain_civilizations
    for y, x in spreading:
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or not area[ny][nx]:
                continue
            p = find(area[y][x])
            np = find(area[ny][nx])
            if p == np:
                continue
            union(p, np)
            remain_civilizations -= 1


def spread():
    global spreading, remain_civilizations

    next_spreading = []
    for y, x in spreading:
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx]:
                continue
            area[ny][nx] = area[y][x]
            next_spreading.append((ny, nx))
            for ddy, ddx in direction:
                nny, nnx = ny + ddy, nx + ddx
                if not oob(nny, nnx) and area[nny][nnx] and find(area[ny][nx]) != find(area[nny][nnx]):
                    union(area[ny][nx], area[nny][nnx])
                    remain_civilizations -= 1
    spreading = next_spreading


N, K = map(int, input().split())
area = [[0] * N for _ in range(N)]

parents = [None] + [i for i in range(1, K + 1)]
spreading = []

for i in range(1, K + 1):
    aa, bb = map(lambda inp: int(inp) - 1, input().split())
    area[aa][bb] = i
    spreading.append((aa, bb))

remain_civilizations = K - 1
check_spreading_near()
time = 0
while remain_civilizations:
    time += 1
    spread()

print(time)
