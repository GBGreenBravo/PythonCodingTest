# 20240725
# 14:23

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    origin = [list(str(input())) for _ in range(n)]

    white = [m - row.count('W') for row in origin]
    blue = [m - row.count('B') for row in origin]
    red = [m - row.count('R') for row in origin]

    mn = n * m
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            mn = min(mn, sum(white[:i] + blue[i:j] + red[j:]))

    print(f"#{test_case} {mn}")




