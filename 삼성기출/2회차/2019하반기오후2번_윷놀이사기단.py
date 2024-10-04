# 20241002
# 29:57
# 1 / 2

# 17825_주사위윷놀이

"""
풀이 시간: 30분 (14:50 - 15:20)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (14:50 - 14:55)
    이전에 했던 대로, 손으로 그리며 칸별 인덱스를 지정했습니다.


2. 구현 (14:55 - 15:09)


3. 디버깅 (15:09 - 15:10)


4. 틀렸습니다 (15:11 - 15:18)
    "print 디버깅 -> 문제 재정독 -> 디버그모드 디버깅"의 과정으로 발견했습니다.
    문제 조건에서 "40이 적혀있는 칸은 도착칸이 아님"을 빠트리고 만족해주지 못해,
    도착지점에 말 1개만 있을 수 있도록 구현해서 틀렸습니다.
"""

scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
          13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0]
connected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 32,
             22, 23, 29, 25, 29, 27, 28, 29, 30, 31, 20, 32]
special_connected = [0] * 33
special_connected[5] = 21
special_connected[10] = 24
special_connected[15] = 26


def dfs(cnt, dfs_arr, score):
    global max_answer

    if cnt == 10:
        max_answer = max(max_answer, score)
        return

    for idx, now in enumerate(dfs_arr):
        if now == 32:
            dfs(cnt + 1, [ar for ar in dfs_arr], score)

        for m in range(movings[cnt]):
            if m == 0 and special_connected[now]:
                now = special_connected[now]
            else:
                now = connected[now]

        if now != 32 and now in dfs_arr:
            continue

        next_dfs_arr = [ar for ar in dfs_arr]
        next_dfs_arr[idx] = now
        dfs(cnt + 1, next_dfs_arr, score + scores[now])


movings = list(map(int, input().split()))

max_answer = 0
dfs(0, [0, 0, 0, 0], 0)
print(max_answer)
