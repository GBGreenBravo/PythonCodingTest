# 20240814
# 03:40
# 1 / 1

t = int(input())
for test in range(1, t + 1):
    n = int(input())
    answer = -1  # 정답이 없는 경우를 대비하여 -1로 초기화

    left = 1
    right = int(n ** (1 / 2))  # n의 3제곱근이 n의 2제곱근보다 큰 경우는 없으므로, right는 루트n으로 설정

    while left <= right:  # 이분탐색
        mid = (left + right) // 2

        mid_value = mid ** 3  # 비교를 위한 mid_value는 mid의 세제곱
        if mid_value == n:
            answer = mid
            break
        elif mid_value > n:
            right = mid - 1
        elif mid_value < n:
            left = mid + 1

    print(f"#{test} {answer}")
