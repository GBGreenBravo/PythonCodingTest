# 20240930
# 10:28
# 1 / 2

# 14888_연산자끼워넣기

"""
풀이 시간: 분 (15:00 - 15:10)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (15:00 - 15:02)


2. 구현 (15:02 - 15:08)


3. 디버깅 (15:08 - 15:09)


4. 틀렸습니다 (15:09 - 15:10)
    1e9와 같은 방식을 평소에 거의 활용하지 않는데, 해당 타입이 int가 아닌 float인줄 인지하지 못하고 있었습니다.
    그래서 최소/최대값이 float로 출력되어 뒤에 .0이 붙었고 오답처리 됐습니다.

    이번 기회에 1e9와 같은 컴퓨터식 지수 표현의 type에 대해 정확하게 알고 가게 됐습니다.
    그렇더라도 다음부터는 안전하게 선언할 때부터 int형을 할당할 예정입니다.
"""


def dfs(cnt, value, plus_cnt, minus_cnt, multiple_cnt):
    global min_answer, max_answer

    if cnt == n - 1:
        min_answer = min(min_answer, value)
        max_answer = max(max_answer, value)
        return

    if plus_cnt:
        dfs(cnt + 1, value + numbers[cnt + 1], plus_cnt - 1, minus_cnt, multiple_cnt)

    if minus_cnt:
        dfs(cnt + 1, value - numbers[cnt + 1], plus_cnt, minus_cnt - 1, multiple_cnt)

    if multiple_cnt:
        dfs(cnt + 1, value * numbers[cnt + 1], plus_cnt, minus_cnt, multiple_cnt - 1)


n = int(input())
numbers = list(map(int, input().split()))
operation_limits = list(map(int, input().split()))

min_answer, max_answer = 1e9 + 1, -1e9 - 1
dfs(0, numbers[0], *operation_limits)
print(min_answer, max_answer)
