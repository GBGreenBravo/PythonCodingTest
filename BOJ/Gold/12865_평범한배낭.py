# 20240817
# 49:27
# 1 / 3

n, k = map(int, input().split())
things = [tuple(map(int, input().split())) for _ in range(n)]
things.sort(key=lambda x: x[0])

max_values_by_weight = [0] * 100_001  # 무게에 따른 최대 가치합을 저장할 배열
for thing in things:
    w, v = thing
    for i in range(100_000, 0, -1):  # 가벼운 것부터 하면 중복 카운트될 수 있어서, 무거운 것부터.
        if max_values_by_weight[i] and i + w < 100_001:  # 이전에 도달 가능한 무게고, 이 무게를 추가한 게 유효한 영역 내일 때
            max_values_by_weight[i + w] = max(max_values_by_weight[i + w], max_values_by_weight[i] + v)  # 가치합 최대값 갱신
    max_values_by_weight[w] = max(max_values_by_weight[w], v)  # 이 thing만 있는 경우

print(max(max_values_by_weight[:k + 1]))  # limit 내에서 최대값 찾아서 출력
