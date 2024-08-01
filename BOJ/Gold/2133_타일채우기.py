# 20240801
# 18:24
# 1 / 1

# 조합이 수직선 상으로 끊기는 포인트를 계산하는 것이 포인트였음.
# 8의 경우, 2222 224 242 422 26 62 44 8 이렇게 끊기는 게 가능한데,
# 2를 제외한 4,6,8,...은 딱 2가지 경우 밖에 없음. (2는 3가지 경우)
# 그렇기에 n의 모든 짝수 조합에 따른 계산만 해주면 됨.
# 더 대중적인 풀이는, 더 간단한 DP

from collections import deque


def solve():
    if n % 2 == 1:
        return 0

    combis = []
    poss = tuple(i for i in range(2, n + 1) if i % 2 == 0)

    queue = deque()
    for p in poss:
        queue.append(([p], p))
    while queue:
        combi, sum = queue.popleft()
        if sum == n:
            combis.append(combi)
            continue
        elif sum > n:
            continue
        elif sum < n:
            for p in poss:
                queue.append((combi + [p], sum + p))

    answer = 0
    for comb in combis:
        tmp = 1
        for c in comb:
            tmp *= 3 if c == 2 else 2
        answer += tmp

    return answer


n = int(input())
print(solve())
