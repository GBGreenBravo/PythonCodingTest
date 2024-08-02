# 20240802
# 42:37
# 1 / 1

from collections import deque


def calculate_pizza_dict(pizza_alpha, len_pizza):  # 피자에 가능한 연속조합별 개수를 dictionary로 반환
    pizza_dict = dict()

    queue = deque()
    for i in range(len_pizza):
        for _ in range(i):
            queue.append(queue.popleft() + pizza_alpha[i])
        queue.append(pizza_alpha[i])

        for j in queue:
            if pizza_dict.get(j):
                pizza_dict[j] += 1
            else:
                pizza_dict[j] = 1

    queue.popleft()
    index = -1
    while queue:
        index += 1
        queue.popleft()
        for _ in range(len_pizza - 2 - index):
            value = queue.popleft() + pizza_alpha[index]
            queue.append(value)

            if pizza_dict.get(value):
                pizza_dict[value] += 1
            else:
                pizza_dict[value] = 1

    return pizza_dict


size = int(input())
m, n = map(int, input().split())
pizza_a = [int(input()) for _ in range(m)]
pizza_b = [int(input()) for _ in range(n)]

pizza_a_dict = calculate_pizza_dict(pizza_a, m)
pizza_b_dict = calculate_pizza_dict(pizza_b, n)

answer = 0
for s in range(size + 1):
    pizza_a_size = s
    pizza_b_size = size - s
    pizza_a_cnt = 1 if s == 0 else 0 if s not in pizza_a_dict.keys() else pizza_a_dict[s]
    pizza_b_cnt = 1 if size - s == 0 else 0 if size - s not in pizza_b_dict.keys() else pizza_b_dict[size - s]

    answer += pizza_a_cnt * pizza_b_cnt

print(answer)
