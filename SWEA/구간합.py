# 20240722

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    now = 0
    for i in range(m):
        now += arr[i]
    max, min = now, now

    for i in range(m, n):
        now -= arr[i - m]
        now += arr[i]
        if now > max:
            max = now
        if now < min:
            min = now

    print(f"#{test_case} {max - min}")