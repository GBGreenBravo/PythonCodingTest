# 20240927
# 17:11
# 1 / 2

# 12100_2048(Easy)

"""
풀이 시간: 17분 (16:32 - 16:48)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (16:32 - 16:34)
    (09/27 한정) 정독&메모 하지 않았습니다..
    문제 정독&메모 루틴의 소중함을 깨달은 하루였습니다.


2. 구현 (16:34 - 16:44)
    이전에 "12100_2048(Easy)"에서 썼던 코드에서, 개인적으로 아쉬웠던 부분이 있었기에,
    해당 풀이를 더욱 합리적으로 구현하려 했습니다.

    제가 선호하는 (벽이 없을 때의) 중력 작용인, 0 지우기를 활용했습니다.


3. 디버깅 (16:44 - 16:46)
    제가 반시계회전에서 zip(*arr)[::-1]과 같은 실수를 자주하는 경향이 있습니다.

    [::-1]을 하기 위해서는 대상이 list여야 하는데, list를 씌워주지 않았던 것을 수정했습니다.


4. 틀렸습니다 (16:46 - 16:48)
    answer = max(answer, max(map(max, arr)))
    최대값을 갱신할 때, 위와 같은 코드를 적었어야 했는데, 아래와 같은 코드를 적었습니다..
    answer = max(map(max, arr))

    max()를 썼다고 너무 생각 없이 구현했습니다.
    최소/최대값 갱신에는 무조건 왼쪽의 재선언하는 변수가 들어가야 함을 더욱 확실하게 인지해야겠습니다.
"""


def dfs(cnt, rotate_flag, arr):
    global answer

    if cnt == 5:
        answer = max(answer, max(map(max, arr)))
        return

    if rotate_flag == 0:
        pass
    elif rotate_flag == 1:
        arr = [list(row)[::-1] for row in zip(*arr)]
    elif rotate_flag == 2:
        arr = [row[::-1] for row in arr[::-1]]
    elif rotate_flag == 3:
        arr = [row for row in list(zip(*arr))[::-1]]

    for row_idx in range(n):
        row = [num for num in arr[row_idx] if num]
        new_row = []

        idx = 0
        while idx <= len(row) - 1:
            if idx == len(row) - 1:
                new_row.append(row[-1])
                break

            if row[idx] == row[idx + 1]:
                new_row.append(row[idx] * 2)
                idx += 2
            else:
                new_row.append(row[idx])
                idx += 1

        arr[row_idx] = new_row + [0] * (n - len(new_row))

    dfs(cnt + 1, 0, [rr[:] for rr in arr])
    dfs(cnt + 1, 1, [rr[:] for rr in arr])
    dfs(cnt + 1, 2, [rr[:] for rr in arr])
    dfs(cnt + 1, 3, [rr[:] for rr in arr])


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

answer = 0
dfs(0, 0, [r[:] for r in area])
dfs(0, 1, [r[:] for r in area])
dfs(0, 2, [r[:] for r in area])
dfs(0, 3, [r[:] for r in area])
print(answer)
