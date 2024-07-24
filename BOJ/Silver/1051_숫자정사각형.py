# 20230723
# 08:44

n, m = map(int, input().split())
rectangle = []
for _ in range(n):
    rectangle.append([int(i) for i in list(str(input()))])

mx = 1

for i in range(n):
    for j in range(m):
        for length in range(1, min(m - j, n - i)):
            if rectangle[i][j] == rectangle[i + length][j] == rectangle[i][j + length] == rectangle[i + length][j + length]:
                mx = max(mx, (length + 1)**2)

print(mx)
