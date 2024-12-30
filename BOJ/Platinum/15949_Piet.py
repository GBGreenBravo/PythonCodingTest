# 20241230
# 27:32
# 1 / 1

from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 동남서북


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def find_index(now_group, dp, cc_left):
    if dp == 0:
        if cc_left:
            return max(group_indexes[now_group], key=lambda mem: (mem[1], -mem[0]))
        else:
            return max(group_indexes[now_group], key=lambda mem: (mem[1], mem[0]))
    elif dp == 1:
        if cc_left:
            return max(group_indexes[now_group], key=lambda mem: (mem[0], mem[1]))
        else:
            return max(group_indexes[now_group], key=lambda mem: (mem[0], -mem[1]))
    elif dp == 2:
        if cc_left:
            return max(group_indexes[now_group], key=lambda mem: (-mem[1], mem[0]))
        else:
            return max(group_indexes[now_group], key=lambda mem: (-mem[1], -mem[0]))
    else:
        if cc_left:
            return max(group_indexes[now_group], key=lambda mem: (-mem[0], -mem[1]))
        else:
            return max(group_indexes[now_group], key=lambda mem: (-mem[0], mem[1]))


def solve():
    answer = area[0][0]
    now_group = group_carved[0][0]
    dp, cc_left = 0, 1

    while True:
        for trying in range(8):
            ny, nx = find_index(now_group, dp, cc_left)
            dy, dx = direction[dp]
            ny, nx = ny + dy, nx + dx
            if oob(ny, nx) or area[ny][nx] == 'X':
                if not trying % 2:
                    cc_left ^= 1
                else:
                    dp = (dp + 1) % 4
            else:
                now_group = group_carved[ny][nx]
                answer += area[ny][nx]
                break
        else:
            break

    print(answer)


N, M = map(int, input().split())
area = [list(str(input())) for _ in range(N)]

group_carved = [[0] * M for _ in range(N)]
group_indexes = [None]
group_flag = 0
for i in range(N):
    for j in range(M):
        if area[i][j] != 'X' and not group_carved[i][j]:
            group_flag += 1
            group_carved[i][j] = group_flag
            group_arr = [(i, j)]
            dq = deque([(i, j)])
            while dq:
                ci, cj = dq.popleft()
                for di, dj in direction:
                    ni, nj = ci + di, cj + dj
                    if oob(ni, nj) or group_carved[ni][nj] or area[ni][nj] != area[i][j]:
                        continue
                    group_carved[ni][nj] = group_flag
                    dq.append((ni, nj))
                    group_arr.append((ni, nj))
            group_indexes.append(group_arr)

solve()
