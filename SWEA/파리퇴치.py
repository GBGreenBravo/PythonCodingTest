# 20240723
# 07:40

def check_flies(flies_list, a, b, r):
    deaths = 0
    for i in range(r):
        for j in range(r):
            deaths += flies_list[a + i][b + j]
    return deaths


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    flies = []
    for _ in range(n):
        flies.append(list(map(int, input().split())))

    mx = -1
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            mx = max(mx, check_flies(flies, i, j, m))

    print(f"#{test_case} {mx}")

