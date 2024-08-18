# 20240818
# 33:26
# 1 / 3


def cal_parts(number, cnt):  # index의 부품을 cnt개 만들기 위해 필요한 최하위 부품 수 배열을 반환하는 함수
    if dp[number]:  # 이미 계산된 값이 있다면
        return [dp[number][i] * cnt for i in range(n + 1)]  # 해당 값 * cnt 해서 반환

    dp[number] = [0 for _ in range(n + 1)]  # number에 대한 필요한 최하위 부품 수 저장할 배열
    for part, part_cnt in parts[number]:  # 필요한 부품과 부품 수에 대해
        get = cal_parts(part, cnt * part_cnt)  # 해당 부품을 필요한 개수만큼 만드는, 최하위 부품 수 배열 호출 (재귀)
        for i in range(n + 1):
            if get[i]:
                dp[number][i] += get[i] // cnt  # dp[]에는 1개 만드는 데에 필요한 최하위 부품 수를 저장하기에, // cnt
    return [dp[number][i] * cnt for i in range(n + 1)]  # 반환할 때는 cnt개 만큼 필요하므로, * cnt


n = int(input())
m = int(input())
parts = [[] for _ in range(n + 1)]
big_parts, small_parts = [], []
for _ in range(m):
    a, b, c = map(int, input().split())
    parts[a].append((b, c))
    big_parts.append(a)
    small_parts.append(b)

small_parts = list(set(small_parts).difference(big_parts))  # m번의 관계들로부터 b의 위치에 있지 않았던 c들, 즉 최하위 부품듣

dp = [0] * (n + 1)  # index의 부품을 만들기 위해 필요한 최하위 부품 수를 명시하는 memoization 배열
for small_part in small_parts:
    dp[small_part] = [0 if i != small_part else 1 for i in range(n + 1)]  # 최하위 부품은 자기 자신 1개만 있으면 됨

answer = cal_parts(n, 1)
for i in range(n + 1):
    if answer[i]:
        print(i, answer[i])
