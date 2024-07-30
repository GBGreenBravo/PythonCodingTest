# 20240730
# 18:59

# 삼각관계로 서로 싫어하는 사람은 없다. 있다면 팀이 3개가 돼야 함.
# 따라서, dfs()로 한 사람에 대해 청팀(0)을 새기고, 그 사람이 싫어하는 사람들은 백팀(1)을 새기고, 이 다음으로 싫어하는 사람들은 청팀(0)을 새긴다.
# 이렇게 visited를 확인하며 dfs를 돌아주면, 모두는 청팀(0)과 백팀(1)로 나뉘게 된다.

def dfs(node, team_index):
    visited[node] = 1
    team_index %= 2
    teams[node] = team_index

    for next in hates[node]:
        if visited[next] == 0:
            dfs(next, team_index + 1)


n = int(input())
hates = [[] for _ in range(n + 1)]
for i in range(n):
    hates[i + 1].extend([int(j) for j in str(input())[2:].split()])

# each_other = [[] for _ in range(n + 1)]  # 서로 싫어하는 정보만 들어오므로 필요 없는 코드.
# for i in range(n + 1):
#     for j in hates[i]:
#         if i in hates[j]:
#             each_other[i].append(j)

teams = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, 0)

blue = [i for i in range(1, n + 1) if teams[i] == 0]
white = [i for i in range(1, n + 1) if teams[i] == 1]

print(len(blue))
print(*sorted(blue))
print(len(white))
print(*sorted(white))


# 위는 재귀 활용, 아래는 스택 활용
"""
n = int(input())
hates = [[] for _ in range(n + 1)]
for i in range(n):
    hates[i + 1].extend([int(j) for j in str(input())[2:].split()])

teams = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        now = i
        visited[now] = 1
        stk = []
        team_index = 0
        teams[now] = team_index % 2

        while True:
            for next in hates[now]:
                if visited[next] == 0:
                    visited[next] = 1
                    stk.append(now)
                    now = next
                    team_index += 1
                    teams[now] = team_index % 2
                    break
            else:
                if stk:
                    now = stk.pop()
                    team_index -= 1
                else:
                    break


blue = [i for i in range(1, n + 1) if teams[i] == 0]
white = [i for i in range(1, n + 1) if teams[i] == 1]

print(len(blue))
print(*sorted(blue))
print(len(white))
print(*sorted(white))
"""