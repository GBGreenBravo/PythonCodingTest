# 20240812
# 52:20
# 1 / 4

def dfs(index, cnt):
    global possible_at_this_limit
    if possible_at_this_limit:  # 이미 가능하면 return
        return

    if cnt == bishop_limit:  # 카운트가 bishop_limit과 동일하다면, 가능하다는 뜻
        possible_at_this_limit = True
        return

    if index == 2 * n - 1:  # 상향대각선 범위 넘으면 return
        return

    if (2 * n - 1) - index < bishop_limit - cnt:  # 앞으로 탐색할 상향대각선보다, 필요한 비숍 개수가 더 크다면 return
        return

    for possible in possibles[index]:  # 현재 index의 상향대각선에 가능한 좌표들에 대해,
        if not visited2[possible[0] - possible[1]]:  # 하향대각선이 겹치지 않는 좌표라면, 방문처리하고 dfs()
            visited2[possible[0] - possible[1]] = True
            dfs(index + 1, cnt + 1)
            visited2[possible[0] - possible[1]] = False

    dfs(index + 1, cnt)  # 현재 index의 상향대각선의 좌표를 활용하지 않는 경우도 존재할 수 있음.


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

possibles = [[] for _ in range(2 * n - 1)]  # 상향 대각선(2n - 1개)별로 비숍 위치가 가능한 좌표들 담는 리스트
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            possibles[i + j].append((i, j))

bishop_limit = 0
possible_at_this_limit = True
while possible_at_this_limit:  # 가능한 비숍 개수면 반복
    bishop_limit += 1
    if bishop_limit == 19:  # 19개의 상향대각선에 1개씩만 존재 가능한데, 처음과 끝 상향대각선은 하향대각선이 무조건 겹치므로 19개는 불가능함.
        break
    possible_at_this_limit = False
    bishop_arr = []
    visited2 = [False] * (2 * n)  # 하향대각선 방문처리를 위한 배열
    dfs(0, 0)

print(bishop_limit - 1)


# 20240808
# 1:18:38
# 0 / 6
# 아래는 틀린 풀이
"""
def dfs(bishop_cnt, start):
    global possible_at_this_answer

    if possible_at_this_answer:
        return

    if len_possible_spaces - start < answer - bishop_cnt:
        return

    if bishop_cnt == answer:
        possible_at_this_answer = True
        return

    if start > len_possible_spaces:
        return

    for i in range(start, len_possible_spaces):
        py, px = possible_spaces[i]
        if not visited_1[py + px] and not visited_2[py - px]:
            visited_1[py + px], visited_2[py - px] = True, True
            bishop_arr.append(possible_spaces[i])
            dfs(bishop_cnt + 1, i + 1)
            bishop_arr.pop()
            visited_1[py + px], visited_2[py - px] = False, False

        if possible_at_this_answer:
            return


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
possible_spaces = []  # 비숍 놓을 수 있는 좌표들
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            possible_spaces.append((i, j))
len_possible_spaces = len(possible_spaces)

answer = 0
while answer < len_possible_spaces:  # 가능할 때까지 answer 하나씩 늘리며 while문
    answer += 1
    possible_at_this_answer = False

    visited_1 = [False] * (2 * n - 1)
    visited_2 = [False] * (2 * n - 1)

    bishop_arr = []
    dfs(0, 0)

    if possible_at_this_answer:
        continue
    else:
        answer -= 1
        break
print(answer)
"""