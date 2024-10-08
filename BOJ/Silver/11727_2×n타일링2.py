# 20240813
# 20:50
# 1 / 2

# 3을 1과 2로만 표현하면, 111 / 21 / 12 가 된다.
# 이 1과 2를 직사각형 세로로 끊은 단위라고 생각하면, 모든 경우가 포함된다.
# 다만, 2를 구성하는 방식이, 2가지이다. -> (1) 가로 1*2 블럭 2개 / (2) 2*2 블럭 1개
# 따라서 111 / 21 / 12 에 대해 모든 자리수를 곱해준 값을 모두 합해주면 정답이 나온다.
# 처음에는 DFS로 1과 2의 조합을 구했는데, n이 100만 돼도 시간복잡도가 너무 커진다.
# 따라서 n을 구성하는 1과 2의 개수만 체크하며 comb(1의개수 + 2의개수, 2의개수)로 1과 2의 조합을 구했다.

from math import comb

n = int(input())
answer = 0

one_cnt = n
two_cnt = 0
while one_cnt >= 0:  # n을 구성하는 1의 개수가 음수가 되면 종료
    answer += comb(one_cnt + two_cnt, two_cnt) * (2 ** two_cnt)  # n에 대해  현재 1/2 카운트의 모든 조합 * 하나의 조합에서 가능한 경우의 수
    one_cnt -= 2  # 2 개수 하나 추가하고
    two_cnt += 1  # 1 개수 둘 빼주기

print(answer % 10_007)


# 아래는 점화식 (dp[n] = dp[n -1] + dp[n - 2] * 2) 으로 푼 풀이
"""
n = int(input())

dp = [0, 1, 3]
for i in range(3, n + 1):
    dp.append(dp[-1] + dp[-2] * 2)

print(dp[n] % 10007)
"""