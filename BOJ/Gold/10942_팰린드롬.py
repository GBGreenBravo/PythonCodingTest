# 20241205
# 1 / 3


def check(start, end):
    if palindrome[start][end] != -1:
        return palindrome[start][end]

    if nums[start] != nums[end]:
        palindrome[start][end] = 0
        return 0

    if start + 1 == end:
        palindrome[start][end] = 1
        return 1

    palindrome[start][end] = check(start + 1, end - 1)
    return palindrome[start][end]


N = int(input())
nums = list(map(int, input().split()))
Q = int(input())
queries = [tuple(map(lambda inp: int(inp) - 1, input().split())) for _ in range(Q)]

palindrome = [[-1] * N for _ in range(N)]
for i in range(N):
    palindrome[i][i] = 1

for s, e in queries:
    print(check(s, e))
