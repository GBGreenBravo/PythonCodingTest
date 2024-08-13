# 20240813
# 58:26
# 1 / 2

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * (max(arr) + 1)  # index의 수가 최대인 증가하는 부분수열 길이를 저장할 배열
for i in range(n):  # arr을 순서대로 돌며
    dp[arr[i]] = max(dp[:arr[i]]) + 1  # 현재 arr[i]가 최대인 부분수열의 최대 길이는, max(arr[i]보다 작은 수들의 증가부분수열 최대길이) + 1 이다.

print(max(dp))
