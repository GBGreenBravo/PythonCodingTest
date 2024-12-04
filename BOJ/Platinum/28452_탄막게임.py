# 20241204
# 40:46
# 1 / 1

direction = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def mht(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)


def solve():
    sy, sx = map(int, input().split())
    k = int(input())
    bullet_inputs = dict()
    for _ in range(k):
        aa, bb = map(int, input().split())
        bullet_inputs[aa * M + bb] = bullet_inputs.get(aa * M + bb, 0) + 1

    visited = [[0] * M for _ in range(N)]
    visited[sy][sx] = 1
    queue = [(sy, sx, bullet_inputs)]

    time = 0
    while queue and time < T:
        next_queue = []
        for y, x, bullets in queue:
            for d_idx, (dy, dx) in enumerate(direction):
                ny, nx = y + dy, x + dx
                if oob(ny, nx):
                    continue
                if d_idx and visited[ny][nx]:
                    continue
                next_bullets = dict()
                for k, v in bullets.items():
                    by, bx = divmod(k, M)
                    candidates = []
                    for bdy, bdx in direction:
                        bny, bnx = by + bdy, bx + bdx
                        if oob(bny, bnx):
                            continue
                        candidates.append((mht(ny, nx, bny, bnx), bny, bnx))
                    dist, bfy, bfx = min(candidates)
                    if not dist:
                        break
                    next_bullets[bfy * M + bfx] = next_bullets.get(bfy * M + bfx, 0) + 1
                else:
                    visited[ny][nx] = 1
                    next_queue.append((ny, nx, next_bullets))

        time += 1
        queue = next_queue

    print("YES" if queue else "NO")


N, M, T = map(int, input().split())
solve()
