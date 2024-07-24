# 20240724
# 03:30

# paper에 1을 표시햐여 종이를 올려줍니다.
# 1로 표시하였기에 전체합을 계산하면 면적을 구할 수 있습니다.

paper = [[0] * 101 for _ in range(101)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            paper[i][j] = 1
print(sum([sum(i) for i in paper]))

