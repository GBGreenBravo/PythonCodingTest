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

# 1:18:38
