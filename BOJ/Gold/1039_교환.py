# 20240930
# 10:03
# 1 / 3

# 방문배열 안 둬서 1번 틀리고,
# 1_000_000인 경우 포함 안 해줘서, IndexError 났음


def dfs(cnt, num_string):
    global max_answer

    if cnt == k:
        max_answer = max(max_answer, int(num_string))
        return

    if visited[cnt][int(num_string)]:
        return
    visited[cnt][int(num_string)] = 1

    for i in range(m - 1):
        if i == 0:
            for j in range(1, m):
                if not int(num_string[j]):
                    continue
                dfs(cnt + 1, num_string[j] + num_string[i + 1:j] + num_string[i] + num_string[j + 1:])
        else:
            for j in range(i + 1, m):
                dfs(cnt + 1, num_string[:i] + num_string[j] + num_string[i + 1:j] + num_string[i] + num_string[j + 1:])


n, k = map(int, input().split())
n = str(n)
m = len(n)

max_answer = -1
visited = [[0] * 1_000_001 for _ in range(k)]
dfs(0, n)
print(max_answer)
