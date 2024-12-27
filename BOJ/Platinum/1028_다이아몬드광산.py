# 20241227
# 46:32
# 1 / 6

R, C = map(int, input().split())
area = [[int(i) for i in str(input())] for _ in range(R)]

down1 = [[0 for _ in range(C)] for _ in range(R)]
down2 = [[0 for _ in range(C)] for _ in range(R)]
up1 = [[0 for _ in range(C)] for _ in range(R)]
up2 = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    for j in range(C):
        if area[i][j]:
            if not i or j == C - 1 or not area[i - 1][j + 1]:
                r, c = i, j
                d = 1
                while r < R and 0 <= c and area[r][c]:
                    down1[r][c] = d
                    r += 1
                    c -= 1
                    d += 1
            if not i or j == 0 or not area[i - 1][j - 1]:
                r, c = i, j
                d = 1
                while r < R and c < C and area[r][c]:
                    down2[r][c] = d
                    r += 1
                    c += 1
                    d += 1

for i in range(R - 1, -1, -1):
    for j in range(C):
        if area[i][j]:
            if i == R - 1 or j == C - 1 or not area[i + 1][j + 1]:
                r, c = i, j
                d = 1
                while 0 <= r and 0 <= c and area[r][c]:
                    up1[r][c] = d
                    r -= 1
                    c -= 1
                    d += 1
            if i == R - 1 or j == 0 or not area[i + 1][j - 1]:
                r, c = i, j
                d = 1
                while 0 <= r and c < C and area[r][c]:
                    up2[r][c] = d
                    r -= 1
                    c += 1
                    d += 1

answer = 0
for i in range(R):
    for j in range(C):
        for k in range(answer + 1, down1[i][j] + 1):
            if j + 2 * (k - 1) >= C:
                break
            if down2[i][j + 2 * (k - 1)] >= k and up1[i][j] >= k and up2[i][j + 2 * (k - 1)] >= k:
                answer = k
print(answer)
