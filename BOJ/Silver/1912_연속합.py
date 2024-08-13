# 20240813
# 06:26
# 1 / 1

n = int(input())
arr = list(map(int, input().split()))

dp = [i for i in arr]  # 현재 index까지의 연속에서 최대값을 저장하는 배열
for i in range(1, n):  # index 1부터 차례로 갱신
    dp[i] = max(dp[i - 1] + dp[i], dp[i])  # max(이전의 연속 최대치 + 현재값, 현재값)을 저장

print(max(dp))  # 저장된 연속치의 최대값을 출력
