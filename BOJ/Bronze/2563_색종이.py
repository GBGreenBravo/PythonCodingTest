# 20240721
# 08:03

paper = [[0] * 100 for _ in range(100)]

case = int(input())
for _ in range(case):
    a, b = map(int, input().split())
    for i in range(a - 1, a + 9):
        for j in range(b - 1, b + 9):
            paper[i][j] += 1

area = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] > 0:
            area += 1

print(area)