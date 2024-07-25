# 20240725
# 23:59

n = int(input())
counselings = [tuple(map(int, input().split())) for _ in range(n)]
mx_profits = [0] * (n + 1)  # mx_profits에 n일에 대한 최대 이익을 저장.

for i in range(1, n + 1):  # n일에 대해 앞에서부터 최대 이익을 계산
    mx = 0
    for j in range(i):  # counselings에 저장된 이전 날들의 정보들을 탐색하며
        now = mx_profits[j]
        if counselings[j][0] <= i - j:  # 오늘 상담 가능한 정보가 들어있다면 더하고
            now += counselings[j][1]
        mx = max(mx, now)
    mx_profits[i] = mx  # 탐색 후 최대값을 저장
print(max(mx_profits))

