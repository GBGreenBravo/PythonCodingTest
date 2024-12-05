# 20241205
# 14:12
# 1 / 1

N = int(input())
people = [int(input()) for _ in range(N)]

answer = 0
before = []
for person in people:
    while before and before[-1][0] < person:
        answer += before[-1][1]
        before.pop()
    answer += 0 if not before else 1 if before[-1][0] != person else before[-1][1] if len(before) == 1 else before[-1][1] + 1
    if before and before[-1][0] == person:
        before[-1][1] += 1
    else:
        before.append([person, 1])

print(answer)
