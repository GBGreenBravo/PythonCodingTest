# 20240719

n, m = map(int, input().split())

drawing = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            drawing[i][j] += 1

count = 0
for i in drawing:
    for j in i:
        if j > m:
            count += 1

print(count)
