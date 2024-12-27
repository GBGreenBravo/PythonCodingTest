# 20241227
# 1:02:24
# 1 / 6

import sys
input = sys.stdin.readline

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))
d_dict = {'N': 0, 'E': 1, 'S': 2, 'W': 3}


def bfs():
    visited = [[[21e9 for _ in range(N)] for _ in range(M)] for _ in range(2**T)]
    visited[0][0][0] = -1
    queue = [(0, 0, 0, 4)]
    time = 0
    while queue:
        next_queue = []
        for collected, y, x, remain in queue:
            now_door = (area[y][x] + time) % 4
            if remain > 1:
                next_queue.append((collected, y, x, remain - 1))

            dy, dx = direction[now_door]
            ny, nx = y + dy, x + dx
            if ny < 0 or M <= ny or nx < 0 or N <= nx:
                continue
            if (ny, nx) in treasure_set:
                collected |= 1 << treasure_dict[(ny, nx)]
            if time >= visited[collected][ny][nx]:
                continue
            visited[collected][ny][nx] = time
            next_queue.append((collected, ny, nx, 4))

        if visited[-1][-1][-1] != 21e9:
            print(time + 1)
            return

        queue = next_queue
        time += 1


while True:
    M, N = map(int, input().split())
    if not M + N:
        break
    area = [[d_dict[i] for i in str(input()).strip()] for _ in range(M)]
    T = int(input())
    treasure_set = set()
    treasure_dict = dict()
    for i in range(T):
        aa, bb = map(lambda inp: int(inp) - 1, input().split())
        treasure_set.add((aa, bb))
        treasure_dict[(aa, bb)] = i
    bfs()
