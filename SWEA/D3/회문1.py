# 20240725
# 16:35

for test_case in range(1, 11):
    p = int(input())
    board = [list(str(input())) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(9 - p):
            i_word = ''
            j_word = ''
            for k in range(p):
                i_word += board[i][j + k]
                j_word += board[j + k][i]
            if i_word == i_word[::-1]:
                cnt += 1
            if j_word == j_word[::-1]:
                cnt += 1
    print(f"#{test_case} {cnt}")

