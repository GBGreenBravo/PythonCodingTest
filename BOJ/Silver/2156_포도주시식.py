# 20241013
# 19:22
# 1 / 2

n = int(input())
wines = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(wines))
    exit()

one_arr = [0, wines[0], wines[1]]
two_arr = [0, wines[0], wines[0] + wines[1]]

for i in range(2, n):
    a = one_arr[-1] + wines[i]
    b = max(one_arr[-2], two_arr[-2], one_arr[-3], two_arr[-3]) + wines[i]
    two_arr.append(a)
    one_arr.append(b)

print(max(one_arr[-1], two_arr[-1], one_arr[-2], two_arr[-2]))
