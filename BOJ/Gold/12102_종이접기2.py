# 20240921
# 34:01
# 1 / 1


# 열(idx-1과 idx 사이)을 접은 배열을 반환하는 함수
def fold_column(paper, idx):
    new_paper = [[0] * max(idx, len(paper[0]) - idx) for _ in range(len(paper))]
    for r in range(len(paper)):
        for c in range(len(paper[0])):
            if c < idx:
                new_paper[r][c - idx] += paper[r][c]
            else:
                new_paper[r][-1 - (c - idx)] += paper[r][c]
    return new_paper


# 행(idx-1과 idx 사이)을 접은 배열을 반환하는 함수
def fold_row(paper, idx):
    new_paper = [[0] * len(paper[0]) for _ in range(max(idx, len(paper) - idx))]
    for c in range(len(paper[0])):
        for r in range(len(paper)):
            if r < idx:
                new_paper[r - idx][c] += paper[r][c]
            else:
                new_paper[-1 - (r - idx)][c] += paper[r][c]
    return new_paper


# 최대값 갱신하고, 접을 수 있는 경우에 대해 접고 재귀함수 호출하는 DFS 함수
def check_and_fold(paper):
    global max_answer
    max_answer = max(max_answer, max(map(max, paper)))

    for col in range(1, len(paper[0])):
        check_and_fold(fold_column(paper, col))
    for row in range(1, len(paper)):
        check_and_fold(fold_row(paper, row))


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

max_answer = min(map(min, area))
check_and_fold(area)  # DFS 호출
print(max_answer)
