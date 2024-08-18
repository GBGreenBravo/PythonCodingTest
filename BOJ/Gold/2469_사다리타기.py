# 20240818
# 14:53
# 1 / 2

k, n = int(input()), int(input())

before = [chr(65 + i) for i in range(k)]
after = list(str(input()))

ladders = [list(str(input())) for _ in range(n)]
for i in range(n):
    if ladders[i][0] == '?':
        hidden_floor = i
        break

for i in range(hidden_floor):
    for j in range(k - 1):
        if ladders[i][j] == '-':
            before[j], before[j + 1] = before[j + 1], before[j]
for i in range(n - 1, hidden_floor, -1):
    for j in range(k - 1):
        if ladders[i][j] == '-':
            after[j], after[j + 1] = after[j + 1], after[j]

answer = ''
for i in range(k - 1):
    if before[i] != after[i]:
        answer += '-'
        before[i], before[i + 1] = before[i + 1], before[i]
    else:
        answer += '*'

if before != after:
    print('x' * (k - 1))
else:
    print(answer)
