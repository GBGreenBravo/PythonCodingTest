# 20240930
# 18:23
# 1 / 1

# 14890_경사로

"""
풀이 시간: 18분 (14:13 - 14:31)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:13 - 14:17)


2. 구현 (14:17 - 14:27)
    이전 풀이와 풀이 방식은 거의 같았지만,
    경사로 설치 유무를 visited배열로 체크한 게 아니라
    최근 경사로 설치 index만 변수 하나로 두고 이를 기준으로 체크했다는 점에서, 개선점이 있었습니다.


3. 디버깅 (14:27 - 14:30)
    경사로를 index기준 -방향으로 깔아야 할 슬라이싱에서,
    row_arr[idx - l + 1:idx + 1]이 아닌 row_arr[idx - l:idx + 1]으로 적었던 실수가 있었습니다.
    인덱스를 활용하는 경우, 더 꼼꼼히 이를 계산해야 할 것으로 생각합니다.
"""


def check(row_arr):
    idx = 0
    used_recent = -1

    while idx < n - 1:
        if row_arr[idx] == row_arr[idx + 1]:
            idx += 1
            continue

        if row_arr[idx] > row_arr[idx + 1]:
            if row_arr[idx] - row_arr[idx + 1] != 1:
                return False

            candidate = row_arr[idx + 1:idx + 1 + l]
            if sum(candidate) != row_arr[idx + 1] * l:
                return False
            for cand in candidate:
                if cand != row_arr[idx + 1]:
                    return False
            used_recent = idx + l
            idx = idx + l
            continue

        if row_arr[idx] < row_arr[idx + 1]:
            if row_arr[idx + 1] - row_arr[idx] != 1:
                return False

            candidate = row_arr[idx - l + 1:idx + 1]
            if sum(candidate) != row_arr[idx] * l:
                return False
            for cand in candidate:
                if cand != row_arr[idx]:
                    return False
            if idx - l + 1 <= used_recent:
                return False
            used_recent = idx
            idx += 1

    return True


n, l = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for row in area:
    if check(row):
        answer += 1
area = [list(row)[::-1] for row in zip(*area)]
for row in area:
    if check(row):
        answer += 1
print(answer)
