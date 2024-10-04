# 20241002
# 41:38
# 1 / 2

# 19236_청소년상어

"""
풀이 시간: 42분 (17:00 - 17:42)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (17:00 - 17:10)


2. 구현 (17:10 - 17:29)
    최근 기출에서 주로 다뤄졌던, 정보의 중복 관리에 대해서 저는 중복으로 관리하지 않는 걸 주로 선택했는데,
    조금이라도 배열이 커지면 다른 이슈가 있을 수도 있기 때문에,
    중복으로 정보를 꼼꼼히 관리하는 걸로 구현 스타일을 전환하고자 했습니다.

    이 문제부터 차근히 위의 전환을 시작할 것으로 계획하고, 구현했습니다.


3. 디버깅 (17:29 - 17:37)


4. 틀렸습니다 (17:37 - 17:42)
    다음 재귀호출을 위해, deepcopy한 배열에 정보를 갱신해야 할 것을, 기존 배열에 정보를 갱신해서 틀렸습니다.

    정보 배열 중복 관리로 구현스타일을 전환하고자 하는데,
    이번 기회에 꼭 경험했어야 할 실수를 경험했다고 생각합니다.
"""

direction = (None, (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
counterclockwise = [None, 2, 3, 4, 5, 6, 7, 8, 1]


def oob(y, x):
    return y < 0 or 4 <= y or x < 0 or 4 <= x


def dfs(score, thieves_info, thieves_area, cy, cx, cd):
    global max_answer
    max_answer = max(max_answer, score)

    for t_idx in range(1, 17):
        if not thieves_info[t_idx]:
            continue

        ty, tx, td = thieves_info[t_idx]

        for dd in range(8):
            if dd:
                td = counterclockwise[td]
            dty, dtx = direction[td]
            nty, ntx = ty + dty, tx + dtx
            if oob(nty, ntx) or (cy == nty and cx == ntx):
                continue

            if thieves_area[nty][ntx]:
                another_t_idx = thieves_area[nty][ntx]

                thieves_info[t_idx] = [nty, ntx, td]
                thieves_info[another_t_idx][0], thieves_info[another_t_idx][1] = ty, tx

                thieves_area[ty][tx], thieves_area[nty][ntx] = another_t_idx, t_idx
            else:
                thieves_info[t_idx] = [nty, ntx, td]
                thieves_area[ty][tx], thieves_area[nty][ntx] = 0, t_idx
            break

    dcy, dcx = direction[cd]
    ncy, ncx = cy + dcy, cx + dcx
    while not oob(ncy, ncx):
        if thieves_area[ncy][ncx]:
            next_thieves_info = [th[:] for th in thieves_info]
            next_thieves_area = [tha[:] for tha in thieves_area]

            added_score = next_thieves_area[ncy][ncx]
            next_chaser = (ncy, ncx, next_thieves_info[added_score][-1])
            next_thieves_info[added_score] = []
            next_thieves_area[ncy][ncx] = 0

            dfs(score + added_score, next_thieves_info, next_thieves_area, *next_chaser)

        ncy, ncx = ncy + dcy, ncx + dcx


thieves = [[] for _ in range(17)]
thieves_map = [[0] * 4 for _ in range(4)]
for inp_row in range(4):
    input_list = list(map(int, input().split()))
    for inp_col in range(4):
        thieves_map[inp_row][inp_col] = input_list[inp_col * 2]
        thieves[input_list[inp_col * 2]] = [inp_row, inp_col, input_list[inp_col * 2 + 1]]

max_answer = 0

first_score = thieves_map[0][0]
chaser = (0, 0, thieves[thieves_map[0][0]][-1])
thieves[first_score] = []
thieves_map[0][0] = 0

dfs(first_score, [th[:] for th in thieves], [thm[:] for thm in thieves_map], *chaser)

print(max_answer)
