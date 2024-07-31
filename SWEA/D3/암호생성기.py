# 20240731
# 06:14

from collections import deque

for _ in range(10):
    test_case = int(input())
    numbers = deque(map(int, input().split()))
    minus_value = 0

    while True:
        now = numbers.popleft()
        minus_value += 1
        if minus_value == 6:
            minus_value = 1
        now -= minus_value
        if now <= 0:
            numbers.append(0)
            break
        else:
            numbers.append(now)

    print(f"#{test_case}", *numbers)
