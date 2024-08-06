# 20240806
# 05:36
# 1 / 1


def dfs(level):
    if level == n:
        print(*arr)
        return

    for i in range(1, n + 1):
        if not visited[i]:  # 현재 배열에 없는 수라면
            visited[i] = 1  # 방문 처리
            arr.append(i)  # 배열에 추가
            dfs(level + 1)  # 재귀 호출
            arr.pop(-1)  # 배열에서 제거
            visited[i] = 0  # 미방문 처리


n = int(input())
arr = []  # 현재의 배열
visited = [0] * (n + 1)  # 중복을 제거하기 위한 리스트
dfs(0)
