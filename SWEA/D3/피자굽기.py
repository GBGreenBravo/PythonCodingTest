# 20240731
# 12:36

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    pizzas = deque(map(int, input().split()))

    pizza_index = 0
    queue = deque()
    for _ in range(n):
        pizza_index += 1
        queue.append([pizza_index, pizzas.popleft()])

    while pizzas or queue:
        now_index, cheese = queue.popleft()
        cheese //= 2
        if cheese == 0 and pizzas:
            pizza_index += 1
            queue.append([pizza_index, pizzas.popleft()])
        elif cheese != 0:
            queue.append([now_index, cheese])

    print(f"#{test_case} {now_index}")
