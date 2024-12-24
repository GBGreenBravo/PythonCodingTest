# 20241224
# 24:12
# 1 / 1

from heapq import heappop, heappush

direction = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


N = int(input())
area = [list(str(input())) for _ in range(N)]
post_offices = set()
for i in range(N):
    for j in range(N):
        if area[i][j] == 'P':
            sy, sx = i, j
        elif area[i][j] == 'K':
            post_offices.add((i, j))
heights = [list(map(int, input().split())) for _ in range(N)]

all_heights = set()
for h in heights:
    all_heights.update(h)

answer = 1_000_000

for now_min in all_heights:
    if heights[sy][sx] < now_min:
        continue
    visited = [[0] * N for _ in range(N)]
    visited[sy][sx] = 1
    now_max = heights[sy][sx]
    delivering = len(post_offices)
    pq = []
    for dy, dx in direction:
        ny, nx = sy + dy, sx + dx
        if not oob(ny, nx):
            visited[ny][nx] = 1
            heappush(pq, (heights[ny][nx], ny, nx))
    while pq and delivering:
        now_height, cy, cx = heappop(pq)
        if now_height < now_min:
            continue
        now_max = max(now_max, now_height)
        if (cy, cx) in post_offices:
            delivering -= 1
        for dy, dx in direction:
            ny, nx = cy + dy, cx + dx
            if not oob(ny, nx) and not visited[ny][nx]:
                visited[ny][nx] = 1
                heappush(pq, (heights[ny][nx], ny, nx))

    if not delivering:
        answer = min(answer, now_max - now_min)

print(answer)
