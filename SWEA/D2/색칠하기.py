# 20240723
# 05:18

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    paper = [[0] * 10 for _ in range(10)]

    for _ in range(n):
        a, b, c, d, color = map(int, input().split())
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                if paper[i][j] == color or paper[i][j] == 3:
                    continue
                else:
                    paper[i][j] += color

    result = 0
    for i in paper:
        for j in i:
            if j == 3:
                result += 1

    print(f"#{test_case} {result}")



