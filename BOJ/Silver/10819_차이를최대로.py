# 202408007
# 55:45
# 1 / 3

# 8!에서 2를 10으로 착각해서 요상한 접근으로 풀다가, 시간이 오래 걸렸던 문제.


def check(arr):  # 문제에서 요구하는 계산식의 값 구하고, 최대값 갱신하는 함수
    sm = 0
    for i in range(n - 1):
        sm += abs(arr[i] - arr[i + 1])

    global answer
    answer = max(answer, sm)


def dfs(cnt, arr):  # 현재까지 순열의 길이, 순열
    if cnt == n:  # 순열 완성되면 check()
        check(arr)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, arr + [array[i]])
            visited[i] = False


n = int(input())
array = list(map(int, input().split()))
visited = [False] * n  # 순열 생성 시 중복 피하기 위한 방문 배열
answer = 0
dfs(0, [])
print(answer)
