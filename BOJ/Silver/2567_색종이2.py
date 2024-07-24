# 20240724
# 06:43

# paper에 1을 표시햐여 종이를 올려줍니다.
#   103으로 설정한 이유는 가상의 테두리 1을 추가해야, 테두리 계산이 수월하기 때문입니다.
# 가로와 세로 방향에 대해 0부터 시작하여 그 값이 몇번을 (0, 1)에서 바뀌는지 세면, 테두리를 계산할 수 있습니다.

paper = [[0] * 103 for _ in range(103)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y + 1, y + 11):
        for j in range(x + 1, x + 11):
            paper[i][j] = 1

sm = 0
for i in range(103):
    now = 0
    for j in range(103):
        if now == paper[i][j]:
            continue
        else:
            now = paper[i][j]
            sm += 1
for i in range(103):
    now = 0
    for j in range(103):
        if now == paper[j][i]:
            continue
        else:
            now = paper[j][i]
            sm += 1

print(sm)
