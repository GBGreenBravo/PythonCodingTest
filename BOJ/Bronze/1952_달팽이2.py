# 20240914
# 1 / 1

# 주로 사용하는 나선형 회전 코드 (area를 visited로 사용함)

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
m, n = map(int, input().split())
area = [[0] * n for _ in range(m)]

answer = 0
y, x, d = 0, 0, 0

while not area[y][x]:
    area[y][x] = 1

    dy, dx = direction[d]
    ny, nx = y + dy, x + dx
    if ny < 0 or m <= ny or nx < 0 or n <= nx or area[ny][nx]:
        answer += 1
        d = (d + 1) % 4
        dy, dx = direction[d]
        ny, nx = y + dy, x + dx

    y, x = ny, nx

print(answer - 1)


# 아래는, 좌표말고 행/열 수만 보면서 나선형 회전
"""
lst = list(map(int, input().split()))
answer = 0
idx = 0
while lst[0] != 1 and lst[1] != 1:
    lst[idx] -= 1
    idx ^= 1
    answer += 1
print(answer + 1)
"""