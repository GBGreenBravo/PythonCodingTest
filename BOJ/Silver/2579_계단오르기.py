# 20240813
# 35:37
# 1 / 1

n = int(input())
stairs = [int(input()) for _ in range(n)]  # 계단의 점수

jump1_2 = [stairs[0]] + [None for _ in range(n - 1)]  # 최근에 두계단 연속 밟은 점수의 최대값 저장
jump2 = [stairs[0]] + [None for _ in range(n - 1)]  # 최근에 점프한 점수의 최대값 저장

for i in range(1, n):  # 0번 인덱스는 따로 처리
    jump1_2[i] = jump2[i - 1] + stairs[i]  # 두계단을 연속으로 밟기 위해서는 이전 계단이 점프한 계단이어야 한다.
    jump2[i] = max(jump1_2[i - 2], jump2[i - 2]) + stairs[i] if i - 2 >= 0 else stairs[i]  # 점프는 -2의 계단이라면 뭐든 상관 없이 최대값 갱신 가능

print(max(jump1_2[-1], jump2[-1]))
