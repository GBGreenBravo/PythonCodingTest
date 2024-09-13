# 20240913
# 05:56
# 1 / 1

# from math import comb
#
# answer = 0
# for i in range(1, 21):
#     answer += comb(20, i)
# print(answer)


def dfs(target_cnt, cnt, start_idx):
    if cnt == target_cnt:
        numbers.add(sum(num_arr))
        return

    for j in range(start_idx, n):
        num_arr.append(lst[j])
        dfs(target_cnt, cnt + 1, j + 1)
        num_arr.pop()


n = int(input())
lst = list(map(int, input().split()))
numbers = set()

for i in range(1, 21):
    num_arr = []
    dfs(i, 0, 0)


for i in range(1, sum(lst) + 2):
    if i not in numbers:
        print(i)
        exit()
