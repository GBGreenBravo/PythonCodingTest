# 20240722
# 03:49

n = int(input())
lst = [float(input()) for _ in range(n)]
answer = max(lst)

for i in range(0, n):
    now = lst[i]
    for j in range(i + 1, n):
        now *= lst[j]
        if now > answer:
            answer = now

print("{0:.3f}".format(answer))


# DP를 활용하여, 시간복잡도 O(N)으로 해결 가능. 위 코드는 O(N**2)였음.
'''
n = int(input())
lst = [float(input()) for _ in range(n)]

answer = lst[0]
now = lst[0]

for i in range(1, n):
    if now < 1:
        now = 1
    now *= lst[i]
    if now > answer:
        answer = now

print(f"{answer:.3f}")
'''
