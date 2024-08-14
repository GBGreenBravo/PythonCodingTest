# 20240814
# 09:09
# 1 / 1

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

left, right = 1, max(budgets)  # left 초기값이 1인 이유는, 각 요청예산은 1이상이고 m은 n이상이 보장돼 있기 때문.
while left <= right:  # 이분탐색
    mid = (left + right) // 2

    mid_value = 0
    for budget in budgets:
        if mid < budget:
            mid_value += mid
        else:
            mid_value += budget

    if mid_value == m:
        right = mid
        break
    elif mid_value < m:
        left = mid + 1
    elif mid_value > m:
        right = mid - 1

print(right)  # 반복문 내의 right는 항상 m보다 큰 value를 가졌지만, 종료(m을 찾거나, left == right가 됐거나) 직전에는 right 값이 m 이하가 되기 때문.
