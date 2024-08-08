# 20240808
# 18:05
# 1 / 1


def dfs(day, sm, is_end):  # 상담날짜 인덱스, 현재까지의 상담 총수익, 더 이상 상담을 못 하는지 여부
    if is_end:  # 더 이상 상담을 진행 못 하면, 최대값 갱신
        global mx
        mx = max(mx, sm)
        return

    # day 인덱스의 상담을 선택하는 경우
    if day + periods[day] > n:  # 상담하면 퇴사일이랑 겹치는 경우
        dfs(day + periods[day], sm, True)
    elif day + periods[day] == n:  # 상담하고 바로 퇴사하는 경우
        dfs(day + periods[day], sm + profits[day], True)
    else:  # 상담해도 퇴사일 남은 경우
        dfs(day + periods[day], sm + profits[day], False)

    # day 인덱스의 상담을 선택하지 않는 경우
    if day + 1 == n:  # 상담 안 하고 퇴사하는 경우
        dfs(day + 1, sm, True)
    else:  # 상담 안 하고 퇴사일 남은 경우
        dfs(day + 1, sm, False)


n = int(input())
periods = [None] * n
profits = [None] * n
for i in range(n):
    i_period, i_profit = map(int, input().split())
    periods[i] = i_period
    profits[i] = i_profit
mx = 0
dfs(0, 0, False)
print(mx)


# dfs() 들어가기 전에 퇴사일 점검 안 해도 되고, (유효하지 않은) 종료 조건으로 return 시켜도 됨.
"""
def dfs(day, sm):  # 상담날짜 인덱스, 현재까지의 상담 총수익, 더 이상 상담을 못 하는지 여부
    if day > n:  # 퇴사날 넘어서까지 상담하는 경우 return
        return

    if day == n:  # 퇴사일에 다다르면, 최대값 갱신
        global mx
        mx = max(mx, sm)
        return

    dfs(day + periods[day], sm + profits[day])  # day 인덱스의 상담을 선택하는 경우
    dfs(day + 1, sm)  # day 인덱스의 상담을 선택하지 않는 경우


n = int(input())
periods = [None] * n
profits = [None] * n
for i in range(n):
    i_period, i_profit = map(int, input().split())
    periods[i] = i_period
    profits[i] = i_profit
mx = 0
dfs(0, 0)
print(mx)
"""

# 20240725
# 23:59

n = int(input())
counselings = [tuple(map(int, input().split())) for _ in range(n)]
mx_profits = [0] * (n + 1)  # mx_profits에 n일에 대한 최대 이익을 저장.

for i in range(1, n + 1):  # n일에 대해 앞에서부터 최대 이익을 계산
    mx = 0
    for j in range(i):  # counselings에 저장된 이전 날들의 정보들을 탐색하며
        now = mx_profits[j]
        if counselings[j][0] <= i - j:  # 오늘 상담 가능한 정보가 들어있다면 더하고
            now += counselings[j][1]
        mx = max(mx, now)
    mx_profits[i] = mx  # 탐색 후 최대값을 저장
print(max(mx_profits))

