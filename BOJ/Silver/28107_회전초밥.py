# 20240812
# 23:14
# 1 / 1

from heapq import heappop, heappush

n, m = map(int, input().split())
customers = [(i, set(list(map(int, input().split()))[1:])) for i in range(n)]
sushis = list(map(int, input().split()))

priorities_by_sushi = [[] for _ in range(200_001)]  # 스시번호에 따른 손님 우선순위를 heapq로 저장
for customer_index, sushi_set in customers:
    for sushi in sushi_set:
        heappush(priorities_by_sushi[sushi], customer_index)

ate_cnt = [0] * n  # 손님별 먹은 개수 카운트
for sushi in sushis:
    if priorities_by_sushi[sushi]:  # heappop() 사용하려면, heapq 안 비어있어야 함.
        ate_cnt[heappop(priorities_by_sushi[sushi])] += 1  # 우선순위 손님의 먹은 개수 += 1
print(*ate_cnt)
