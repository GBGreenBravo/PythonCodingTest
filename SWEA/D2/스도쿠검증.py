# 20240724
# 30:45

# 2차원 리스트에서 칼럼을 추출하는 방법은,
# lst[:][colulmn] 이 아닌
# [row[column] for row in lst] 이다.
# 추가로 zip() 활용하면 list(zip(*lst))[column]도 가능.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def verify_box(board):
    for y in range(3):
        for x in range(3):
            ny = y * 3
            nx = x * 3
            box = board[ny][nx: nx + 3] + board[ny + 1][nx:nx + 3] + board[ny + 2][nx:nx + 3]
            if sorted(box) != nums:
                return False
    return True


def verify_row(board):
    for row in range(9):
        if sorted(board[row]) != nums:
            return False
    return True


def verify_column(board):
    for column in range(9):
        if sorted([i[column] for i in board]) != nums:
            return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    correct = False
    if verify_box(sudoku) and verify_row(sudoku) and verify_column(sudoku):
        correct = True
    print(f"#{test_case} {1 if correct else 0}")

