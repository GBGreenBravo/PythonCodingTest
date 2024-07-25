# 20240725
# 07:47

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    pascal = [[1]] + [[1] * 2 for i in range(9)]

    for i in range(2, 10):
        for j in range(i - 1):
            pascal[i].insert(j + 1, pascal[i - 1][j] + pascal[i - 1][j + 1])

    print(f"#{test_case}")
    for i in range(n):
        print(*pascal[i], sep=" ")



