# 20241014
# 1 / 1
# 03:51

n = int(input())

nums = [1] * 10

for _ in range(n - 1):
    new_nums = [nums[0]] + [0] * 9
    for i in range(1, 10):
        new_nums[i] = sum(nums[:i + 1])
    nums = new_nums

print(sum(nums) % 10_007)
