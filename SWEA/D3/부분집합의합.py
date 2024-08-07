# 20240806
# 05:19
# 1 / 1


def dfs(cnt, sm, start):  # 이제까지 추가한 수의 개수, 추가한 수의 합, 다음으로 탐색 시작할 index
    if sm > k:  # 조기 종료 조건 : sm이 이미 k보다 크다면
        return

    if cnt == n:  # cnt가 n과 같다면 return
        if sm == k:  # 합이 k와 같다면
            global answer
            answer += 1
        return

    for i in range(start, 13):
        dfs(cnt + 1, sm + i, i + 1)


t = int(input())
for test in range(1, t + 1):
    n, k = map(int, input().split())
    arr = [i for i in range(1, 13)]
    answer = 0
    dfs(0, 0, 1)
    print(f"#{test} {answer}")


# 비트마스킹 플이
"""
t = int(input())
for test in range(1, t + 1):
    n, k = map(int, input().split())
    lst = [i for i in range(1, 13)]
    answer = 0

    for bits in range(1, 2 ** 12):
        sm, cnt = 0, 0
        for pos in range(12):
            if ((bits >> pos) & 1) == 1:
                # print(bits >> pos)
                cnt += 1
                sm += lst[pos]

        if cnt == n and sm == k:
            answer += 1

    print(f"#{test} {answer}")
"""