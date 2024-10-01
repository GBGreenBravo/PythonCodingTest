# 20240930
# 11:00
# 1 / 1

# 14889_스타트와링크

"""
풀이 시간: 11분 (14:01 - 14:12)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:01 - 14:04)


2. 구현 (14:04 - 14:10)
    ij와 ji를 ij로 통합시키고,
    아침에 하는 일만 DFS로 n//2개 만큼 조합을 구성한 후에, 해당 조합을 바탕으로 최소값을 갱신했습니다.


3. 디버깅 (-)
"""


def dfs(cnt, start_idx):
    global min_answer

    if cnt == n // 2:
        now1, now2 = 0, 0
        opposite = [ii for ii in range(n) if ii not in dfs_arr]
        for ii in range(n // 2 - 1):
            for jj in range(ii + 1, n // 2):
                now1 += area[dfs_arr[ii]][dfs_arr[jj]]
                now2 += area[opposite[ii]][opposite[jj]]

        min_answer = min(min_answer, abs(now1 - now2))
        return

    for idx in range(start_idx, n):
        dfs_arr.append(idx)
        dfs(cnt + 1, idx + 1)
        dfs_arr.pop()


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        area[i][j] += area[j][i]

min_answer = sum(map(sum, area))
dfs_arr = []
dfs(0, 0)
print(min_answer)
