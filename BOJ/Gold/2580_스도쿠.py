# 20240816
# 18:52
# 1 / 1


def dfs(cnt):
    global answer_arr
    if answer_arr:  # 정답 찾았다면 return
        return

    if cnt == len_empties:  # 목표치만큼 유효한 숫자들 채웠다면
        answer_arr = [i for i in empty_arr]  # 정답배열에 담고 return
        return

    empty_y, empty_x = empties[cnt]  # 현재 cnt에서 채워야 하는 빈 좌표

    candidates = set(range(1, 10))  # 1~9
    candidates = candidates.difference(set([board[i][empty_x] for i in range(9)]))  # row에 존재하는 값 제거
    candidates = candidates.difference(set([board[empty_y][i] for i in range(9)]))  # column에 존재하는 값 제거

    sy, sx = empty_y, empty_x  # 현재 빈 좌표가 속한 구역의 좌상단 좌표 찾는 과정
    while sy % 3 != 0:
        sy -= 1
    while sx % 3 != 0:
        sx -= 1
    candidates = candidates.difference(set([board[sy + dy][sx + dx] for dy in range(3) for dx in range(3)]))  # 현재 3*3 구역에 존재하는 값 제거

    for num in candidates:
        board[empty_y][empty_x] = num
        empty_arr.append(num)
        dfs(cnt + 1)
        empty_arr.pop()
        board[empty_y][empty_x] = 0

        if answer_arr:
            return


board = [list(map(int, input().split())) for _ in range(9)]
empties = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            empties.append((i, j))  # 채워줘야 하는(0으로 채워져있는) 좌표 저장

empty_arr = []  # DFS/백트래킹 하며 순서대로 숫자들이 저장될 배열
len_empties = len(empties)  # 채워야 하는 숫자 개수 목표치

answer_arr = None  # 정답이 담길 배열
dfs(0)

for i in range(len_empties):
    y, x = empties[i]
    board[y][x] = answer_arr[i]  # 빈 좌표에 정답 숫자들 채워주기

for row in board:
    print(*row)
