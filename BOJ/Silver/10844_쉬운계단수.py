# 20241014
# 04:37
# 1 / 1

n = int(input())
lst = [1] * 10
for _ in range(n - 1):
    new_lst = [lst[1]] + [0] * 8 + [lst[-2]]
    for i in range(1, 9):
        new_lst[i] = (lst[i - 1] + lst[i + 1]) % 1_000_000_000
    lst = new_lst
print(sum(lst[1:]) % 1_000_000_000)
