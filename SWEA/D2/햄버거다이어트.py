# 20240807
# 07:11
# 1 / 1


def dfs(taste, calories, start):  # 맛 총합, 칼로리 총합, 이 함수에서 다음으로 탐색 시작할 materials의 index
    global answer

    if calories > l:  # 이미 칼로리제한 초과면 조기 종료
        return

    if taste > answer:  # taste가 answer보다 크다면 answer 갱신
        answer = taste

    if start == n:  # materials 마지막까지 탐색 끝났다면 종료
        return

    for i in range(start, n):
        dfs(taste + materials[i][0], calories + materials[i][1], i + 1)


t = int(input())
for test in range(1, t + 1):
    n, l = map(int, input().split())
    materials = [tuple(map(int, input().split())) for _ in range(n)]

    answer = 0
    dfs(0, 0, 0)

    print(f"#{test} {answer}")
