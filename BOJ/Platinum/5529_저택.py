# 20250110
# 1:34:16
# 1 / 9

# 현재 스위치 칸에서 상하좌우로 갔을 때 최초로 만나는 친구만 점검해도 되는데,
# 상하좌우 끝까지 다 한번에 queue에 넣으려고 해서 시간초과났던 문제.

from heapq import heappop, heappush

M, N, K = map(int, input().split())
row_switches = dict()
col_switches = dict()
visited = dict()
for _ in range(K):
    aa, bb = map(int, input().split())
    visited[(bb, aa)] = N * M + 2
    row_switches[bb] = row_switches.get(bb, []) + [(bb, aa)]
    col_switches[aa] = col_switches.get(aa, []) + [(bb, aa)]
row_switches[N] = row_switches.get(N, []) + [(N, M)]
col_switches[M] = col_switches.get(M, []) + [(N, M)]
visited[(N, M)] = N * M + 2
row_indexes = dict()
col_indexes = dict()
for k, v in row_switches.items():
    v.sort()
    for idx, (y, x) in enumerate(v):
       row_indexes[(y, x)] = idx
for k, v in col_switches.items():
    v.sort()
    for idx, (y, x) in enumerate(v):
       col_indexes[(y, x)] = idx

queue = []
for sy, sx in col_switches.get(1, []):
    visited[(sy, sx)] = sy - 1
    heappush(queue, (sy - 1, sy, sx, 1))

while queue:
    time, y, x, col_opened = heappop(queue)

    if time != visited[(y, x)]:
        continue

    if y == N and x == M:
        print(time)
        break

    if col_opened:
        rs = row_switches.get(y, [(y, x)])
        rsi = row_indexes[(y, x)]
        rsi_minus = rsi - 1
        if rsi_minus >= 0:
            ny, nx = rs[rsi_minus]
            next_time = time + 1 + abs(nx - x)
            if next_time < visited[(ny, nx)]:
                visited[(ny, nx)] = next_time
                heappush(queue, (next_time, ny, nx, 0))
        rsi_plus = rsi + 1
        if rsi_plus < len(rs):
            ny, nx = rs[rsi_plus]
            next_time = time + 1 + abs(nx - x)
            if next_time < visited[(ny, nx)]:
                visited[(ny, nx)] = next_time
                heappush(queue, (next_time, ny, nx, 0))

        cs = col_switches.get(x, [(y, x)])
        csi = col_indexes[(y, x)]
        csi_minus = csi - 1
        if csi_minus >= 0:
            ny, nx = cs[csi_minus]
            next_time = time + abs(ny - y)
            if next_time < visited[(ny, nx)]:
                visited[(ny, nx)] = next_time
                heappush(queue, (next_time, ny, nx, 1))
        csi_plus = csi + 1
        if csi_plus < len(cs):
            ny, nx = cs[csi_plus]
            next_time = time + abs(ny - y)
            if next_time < visited[(ny, nx)]:
                visited[(ny, nx)] = next_time
                heappush(queue, (next_time, ny, nx, 1))

    if not col_opened:
        rs = row_switches.get(y, [(y, x)])
        rsi = row_indexes[(y, x)]
        rsi_minus = rsi - 1
        if rsi_minus >= 0:
            ny, nx = rs[rsi_minus]
            next_time = time + abs(nx - x)
            if next_time < visited[(ny, nx)]:
                visited[(ny, nx)] = next_time
                heappush(queue, (next_time, ny, nx, 0))
        rsi_plus = rsi + 1
        if rsi_plus < len(rs):
            ny, nx = rs[rsi_plus]
            next_time = time + abs(nx - x)
            if next_time < visited[(ny, nx)]:
                visited[(ny, nx)] = next_time
                heappush(queue, (next_time, ny, nx, 0))

        cs = col_switches.get(x, [(y, x)])
        csi = col_indexes[(y, x)]
        csi_minus = csi - 1
        if csi_minus >= 0:
            ny, nx = cs[csi_minus]
            next_time = time + 1 + abs(ny - y)
            if next_time < visited[(ny, nx)]:
                visited[(ny, nx)] = next_time
                heappush(queue, (next_time, ny, nx, 1))
        csi_plus = csi + 1
        if csi_plus < len(cs):
            ny, nx = cs[csi_plus]
            next_time = time + 1 + abs(ny - y)
            if next_time < visited[(ny, nx)]:
                visited[(ny, nx)] = next_time
                heappush(queue, (next_time, ny, nx, 1))
else:
    print(-1)
