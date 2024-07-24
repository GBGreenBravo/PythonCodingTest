# 20240723
# 06:52

n = int(input())

paper = [[-1] * 1001 for _ in range(1001)]

for index in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a, a + c):
        for j in range(b, b + d):
            paper[i][j] = index

result = [0] * n
for i in range(1001):
    for j in range(1001):
        if paper[i][j] != -1:
            result[paper[i][j]] += 1

print(*result, sep="\n")


# paper의 최소, 최대 좌표를 구해서 압축하면, 시간 더 단축시킬 수 있음.
