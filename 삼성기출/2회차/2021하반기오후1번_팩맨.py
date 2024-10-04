# 20241004
# 45:55
# 1 / 2

# 23290_마법사상어와복제

"""
풀이 시간: 46분 (19:13 - 19:59)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (19:13 - 19:21)
    이전 구상에서는 물고기 각각을 관리했지만,
    이번 구상에서는 칸별 물고기 방향에 따른 개수로 관리를 했습니다.

    이전 풀이에 틀렸던 부분은, 상어의 이동 DFS에서 문제에서 요구하지 않은 중복방문 방지를 했었습니다.
    따라서, 최대한 지문 위주로 읽고 구상하려 노력했습니다.


2. 구현 (19:21 - 19:42)


3. 디버깅 (19:42 - 19:50)
    di, dj = direction_4[d_idx]라고 써야할 부분에 di, dj = direction_4[di]로 써서 다른 답변이 나왔습니다.
    진작에 발견됐어야 할 오타지만, 코드 앞부분에서 di를 다른 변수로 한번 썼기에, 빨리 발견하지 못했습니다.

    이러한 경우에 소모되는 시간을 줄이기 위해, 전역변수명도 한번 쓴 건 쓰지 않도록 주의해야겠습니다.


4. 틀렸습니다 (19:51 - 19:58)
    몬스터가 없는 칸인데도, 시체 남김 처리를 해서 틀렸습니다.
    디버깅에 애를 먹을 수도 있었지만, 천천히 코드를 정독하다가 운이 좋게 발견한 것 같습니다.
    그렇지만, 이번 경험을 통해, 코드 정독 시 최대한 문제 지문을 바탕으로
    (다른 사람의 코드라 생각하고) 비판적인 정독이 가능해진 것 같다는 점을 회고해 봅니다.
"""

direction_8 = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
direction_4 = ((-1, 0), (0, -1), (1, 0), (0, 1))


def oob(y, x):
    return y < 0 or 4 <= y or x < 0 or 4 <= x


def dfs(cnt, moving_y, moving_x, index_arr, killing_cnt):
    if cnt == 3:
        candidates.append((-killing_cnt, [da for da in direction_arr]))
        return

    for m_idx in range(4):
        dmy, dmx = direction_4[m_idx]
        nmy, nmx = moving_y + dmy, moving_x + dmx
        if oob(nmy, nmx):
            continue
        next_killing_cnt = killing_cnt + sum(area[nmy][nmx]) if (nmy, nmx) not in index_arr else killing_cnt
        direction_arr.append(m_idx)
        dfs(cnt + 1, nmy, nmx, index_arr + [(nmy, nmx)], next_killing_cnt)
        direction_arr.pop()


m, t = map(int, input().split())
man_y, man_x = map(lambda inp: int(inp) - 1, input().split())
area = [[[0] * 8 for _ in range(4)] for _ in range(4)]
for _ in range(m):
    aa, bb, cc = map(lambda inp: int(inp) - 1, input().split())
    area[aa][bb][cc] += 1

death_log = [[0] * 4 for _ in range(4)]

for _ in range(t):
    copied_area = [[col[:] for col in row] for row in area]

    next_area = [[[0] * 8 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for d in range(8):
                if area[i][j][d]:
                    now_d = d
                    for __ in range(8):
                        di, dj = direction_8[now_d]
                        ni, nj = i + di, j + dj
                        if oob(ni, nj) or death_log[ni][nj] or (man_y == ni and man_x == nj):
                            now_d = (now_d + 1) % 8
                            continue
                        next_area[ni][nj][now_d] += area[i][j][d]
                        break
                    else:
                        next_area[i][j][d] += area[i][j][d]
    area = next_area

    candidates = []
    direction_arr = []

    dfs(0, man_y, man_x, [], 0)

    next_d_idxs = min(candidates)[-1]
    for d_idx in next_d_idxs:
        di, dj = direction_4[d_idx]
        man_y, man_x = man_y + di, man_x + dj
        if sum(area[man_y][man_x]):
            area[man_y][man_x] = [0] * 8
            death_log[man_y][man_x] = 3

    for i in range(4):
        for j in range(4):
            if death_log[i][j]:
                death_log[i][j] -= 1
            for d in range(8):
                area[i][j][d] += copied_area[i][j][d]

print(sum([sum(area[row][col]) for col in range(4) for row in range(4)]))
