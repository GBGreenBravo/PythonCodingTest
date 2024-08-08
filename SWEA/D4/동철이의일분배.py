# 20240807
# 1:09:48
# 1 / 5


def dfs(person, probability):
    global mx

    if probability <= mx:
        return

    if person == n:
        mx = max(mx, probability)
        return

    for work in range(n):
        if not visited[work]:
            visited[work] = True
            dfs(person + 1, probability * probabilities[person][work])
            visited[work] = False


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    probabilities = [[i / 100 for i in list(map(int, input().split()))] for _ in range(n)]

    visited = [False] * n
    mx = 0
    dfs(0, 1)

    print(f"#{test}", format(mx * 100, ".6f"))
