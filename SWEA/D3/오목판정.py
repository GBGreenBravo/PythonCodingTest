# 20240724
# 17:40

# 2차원 리스트를 우측으로 회전시키는 인덱스 전환은 아래와 같다.
# (i, j) -> ((j + N) % N, (N - 1) - i)

def check_row(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0]) - 4):
            if arr[i][j:j + 5] == ['o', 'o', 'o', 'o', 'o']:
                return True
    return False


def check_diagonal(arr):
    for i in range(len(arr) - 4):
        for j in range(len(arr) - 4):
            if [arr[i + k][j + k] for k in range(5)] == ['o', 'o', 'o', 'o', 'o']:
                return True
    return False


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(str(input())) for _ in range(n)]
    right_spin_board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            right_spin_board[(j + n) % n][n - i - 1] = board[i][j]

    five_in_a_row = False
    if check_row(board) or check_row(right_spin_board) or check_diagonal(board) or check_diagonal(right_spin_board):
        five_in_a_row = True

    print(f"#{test_case} {'YES' if five_in_a_row else 'NO'}")


# 회전하지 않는 경우도 연습
"""
def check_row(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0]) - 4):
            if arr[i][j:j + 5] == ['o', 'o', 'o', 'o', 'o']:
                return True
    return False


def check_column(arr):
    for i in range(len(arr) - 4):
        for j in range(len(arr)):
            if [arr[row][j] for row in range(i, i + 5)] == ['o', 'o', 'o', 'o', 'o']:
                return True
    return False


def check_right_down_diagonal(arr):
    for i in range(len(arr) - 4):
        for j in range(len(arr) - 4):
            if [arr[i + k][j + k] for k in range(5)] == ['o', 'o', 'o', 'o', 'o']:
                return True
    return False


def check_left_down_diagonal(arr):
    for i in range(len(arr) - 4):
        for j in range(4, len(arr)):
            if [arr[i + k][j - k] for k in range(5)] == ['o', 'o', 'o', 'o', 'o']:
                return True
    return False


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(str(input())) for _ in range(n)]
    right_spin_board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            right_spin_board[(j + n) % n][n - i - 1] = board[i][j]

    five_in_a_row = False
    if check_row(board) or check_column(board) or check_right_down_diagonal(board) or check_left_down_diagonal(board):
        five_in_a_row = True

    print(f"#{test_case} {'YES' if five_in_a_row else 'NO'}")
"""