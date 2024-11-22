# 20241122
# 17:50
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or H <= y or x < 0 or W <= x


def dfs(cnt, now_answer):
    global answer

    if answer != -1 and now_answer >= answer:
        return

    if cnt == dirt_cnt:
        answer = now_answer
        return

    for idx in range(dirt_cnt):
        if idx in dfs_arr:
            continue
        between = connected[dfs_arr[-1]][idx]
        if not between:
            continue
        dfs_arr.append(idx)
        dfs(cnt + 1, now_answer + between)
        dfs_arr.pop()


while True:
    W, H = map(int, input().split())
    if not W + H:
        break

    area = [list(str(input())) for _ in range(H)]

    dirt = []
    dirt_cnt = 0
    for i in range(H):
        for j in range(W):
            if area[i][j] == 'o':
                dirt_cnt += 1
                area[i][j] = '.'
                dirt.insert(0, (i, j))
            elif area[i][j] == '*':
                dirt_cnt += 1
                area[i][j] = '.'
                dirt.append((i, j))

    set_dirt = set(dirt)
    connected = [[0] * dirt_cnt for _ in range(dirt_cnt)]

    for i in range(dirt_cnt):
        si, sj = dirt[i]

        visited = [[0] * W for _ in range(H)]
        visited[si][sj] = 1

        queue = deque()
        queue.append((si, sj))

        while queue:
            ci, cj = queue.popleft()
            distance = visited[ci][cj]

            for di, dj in direction:
                ni, nj = ci + di, cj + dj
                if oob(ni, nj) or visited[ni][nj] or area[ni][nj] == 'x':
                    continue
                if (ni, nj) in set_dirt:
                    connected[i][dirt.index((ni, nj))] = distance
                visited[ni][nj] = distance + 1
                queue.append((ni, nj))

    answer = -1
    dfs_arr = [0]
    dfs(1, 0)
    print(answer)
