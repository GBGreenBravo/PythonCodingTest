# 20240730
# 43:07

# 값이 1인 좌표에서 mx+1 만큼의 길이의 인덱스를 다 비교할 필요 없이,
# 첫행과 첫열을 모두 arr 값으로 채워놓고,
# 1인 좌표에서만, ([-1][-1], [-1][], [][-1])의 최소값에서 +1해주는 방식으로 누적시키면 됨.

n, m = map(int, input().split())
arr = [[int(i) for i in list(str(input()))] for _ in range(n)]

result = [[0] * m for _ in range(n)]
for i in range(n):
    result[i][0] = arr[i][0]
for j in range(m):
    result[0][j] = arr[0][j]

for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 0:
            continue
        else:
            result[i][j] = min(result[i - 1][j - 1], result[i][j - 1], result[i - 1][j]) + 1

print(max([max(row) for row in result]) ** 2)
