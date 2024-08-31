# 20240826
# 1:05:30
# 1 / 5

d, n = map(int, input().split())
depths = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

small_oven = 0
small_ovens = []  # 가장 깊은 오븐부터 내림차순 지름에 해당되는 (지름, 깊이 index) 저장
for i in range(d - 1, -1, -1):
    now_oven = depths[i]
    while small_ovens and small_ovens[-1][0] >= now_oven:  # small_ovens[-1][0] > now_oven 조건에서는 시간초과 났음.
        small_ovens.pop()
    small_ovens.append((now_oven, i))

now_depth = d
for pizza in pizzas:
    now_depth -= 1  # 이전 피자 쌓은 곳보다 한칸 더 높이 쌓아야 함.
    if small_ovens and pizza > small_ovens[0][0]:  # 만약 지금 피자 지름보다 좁은 곳이 있다면,
        while small_ovens and pizza > small_ovens[0][0]:
            now_depth = min(now_depth, small_ovens[0][1] - 1)  # 더 좁은 곳보다 한칸 더 높게 (현재 높이 index가 더 작을 수도 있으므로 min()으로 갱신)
            del small_ovens[0]

    if now_depth < 0:  # 피자 쌓으려는 곳이 오븐깊이 벗어나면
        print(0)
        break
else:
    print(now_depth + 1)  # 오븐 깊이 index + 1 출력


# deque 쓰니까 7000ms -> 264ms
"""
from collections import deque

d, n = map(int, input().split())
depths = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

small_oven = 0
small_ovens = deque()  # 가장 깊은 오븐부터 내림차순 지름에 해당되는 (지름, 깊이 index) 저장
for i in range(d - 1, -1, -1):
    now_oven = depths[i]
    while small_ovens and small_ovens[-1][0] >= now_oven:  # small_ovens[-1][0] > now_oven 조건에서는 시간초과 났음.
        small_ovens.pop()
    small_ovens.append((now_oven, i))

now_depth = d
for pizza in pizzas:
    now_depth -= 1  # 이전 피자 쌓은 곳보다 한칸 더 높이 쌓아야 함.
    if small_ovens and pizza > small_ovens[0][0]:  # 만약 지금 피자 지름보다 좁은 곳이 있다면,
        while small_ovens and pizza > small_ovens[0][0]:
            now_depth = min(now_depth, small_ovens[0][1] - 1)  # 더 좁은 곳보다 한칸 더 높게 (현재 높이 index가 더 작을 수도 있으므로 min()으로 갱신)
            small_ovens.popleft() 

    if now_depth < 0:  # 피자 쌓으려는 곳이 오븐깊이 벗어나면
        print(0)
        break
else:
    print(now_depth + 1)  # 오븐 깊이 index + 1 출력
"""