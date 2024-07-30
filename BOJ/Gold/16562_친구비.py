# 20240730
# 09:30

import sys
sys.setrecursionlimit(10000)


def dfs(node, flag1):
    visited[node] = flag1
    for next in relations[node]:
        if visited[next] == 0:
            dfs(next, flag1)


n, m, pocket = map(int, input().split())
costs = list(map(int, input().split()))
relations = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    relations[a].append(b)
    relations[b].append(a)

flag = 1
visited = [0] * n
for i in range(n):
    if visited[i] == 0:
        dfs(i, flag)
        flag += 1

answer = 0
for group_flag in range(1, max(visited) + 1):
    friends = [i for i in range(n) if visited[i] == group_flag]
    if not friends:
        continue
    mn = 10001
    for friend in friends:
        mn = min(mn, costs[friend])

    answer += mn

print(f"{'Oh no' if answer > pocket else answer}")


# 위는 재귀 활용, 아래는 스택 활용
"""
n, m, pocket = map(int, input().split())
costs = list(map(int, input().split()))
relations = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    relations[a].append(b)
    relations[b].append(a)

visited = [0] * n
answer = 0
for i in range(n):
    if visited[i] == 0:
        now = i
        visited[now] = 1
        stk = []
        mn_cost = costs[now]

        while True:
            for next in relations[now]:
                if visited[next] == 0:
                    visited[next] = 1
                    stk.append(now)
                    now = next
                    mn_cost = min(mn_cost, costs[now])
                    break
            else:
                if stk:
                    now = stk.pop()
                else:
                    break

        answer += mn_cost

print(f"{'Oh no' if answer > pocket else answer}")
"""