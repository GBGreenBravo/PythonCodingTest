# 20240806
# 04:13
# 1 / 1


def dfs(level, arr, before):  # 현재 배열에 추가된 수의 개수, 현재 배열, 이전에 추가된 수
    if level == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if not visited[i] and before < i:  # 중복되는 조합이 있으면 안되고 오름차순 정렬이기 때문에, before < i
            visited[i] = 1
            dfs(level + 1, arr + [i], i)
            visited[i] = 0


n, m = map(int, input().split())
visited = [0] * (n + 1)  # 같은 수가 중복으로 배열에 추가되지 않도록 visited 처리
dfs(0, [], 0)


# visited 활용까지 필요없는 문제임. 간단하게 풀 수 있는 건, 간단하게 풀 수 있어야 함!
"""
def dfs(cnt, lst, start):
    if cnt == m:
        print(*lst)
        return

    for i in range(start, n + 1):
        dfs(cnt + 1, lst + [i], i + 1)


n, m = map(int, input().split())
dfs(0, [], 1)
"""