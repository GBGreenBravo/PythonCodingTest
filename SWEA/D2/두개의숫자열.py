# 20240723
# 08:10

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if m < n:
        n, m = m, n
        a, b = b, a

    mx = -2000 * n
    for i in range(m - n + 1):
        now = 0
        for j in range(n):
            now += a[j] * b[i + j]
        mx = max(mx, now)

    print(f"#{test_case} {mx}")

