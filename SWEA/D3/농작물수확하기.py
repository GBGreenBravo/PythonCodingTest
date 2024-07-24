# 20240723
# 12:05

# farm을 2차원리스트로 받고, 마름모꼴로 시작/끝 인덱스를 설정하여 value에 += 해줬습니다.

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    farm = [[int(i) for i in list(str(input()))] for _ in range(n)]
    value = 0
    for i in range(n):
        start = abs(n // 2 - i)
        end = n - start
        value += sum(farm[i][start:end])
    print(f"#{test_case} {value}")


# 슬라이싱이랑 sum() 쓰지 말고 직접 구현하면, 아래와 같이.
"""
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    farm = [[int(i) for i in list(str(input()))] for _ in range(n)]
    value = 0
    half_index = n // 2
    for i in range(half_index + 1):
        value += farm[i][half_index]
        for j in range(1, i + 1):
            value += farm[i][half_index - j]
            value += farm[i][half_index + j]
    for i in range(half_index + 1, n):
        value += farm[i][half_index]
        for j in range(1, n - i):
            value += farm[i][half_index - j]
            value += farm[i][half_index + j]
    print(f"#{test_case} {value}")
"""