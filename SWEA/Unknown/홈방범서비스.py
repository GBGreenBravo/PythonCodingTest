# 20241007
# 1:38:00
# 1 / 1

# 1. 구상단계에서 무의식적으로 조금 더 복잡한, 시간 효율적인 풀이를 생각했음.
#    심지어 틀렸던 구상이라, 해당 실수를 디버깅으로 잡아내기까지 40분 걸림

# 2. 배열의 슬라이싱에 대한 이해 부족으로, 디버깅에 30분 쓰임.
#    print([1, 2, 3, 4][-1:6])
#    위 코드로 출력되는 값은, [1, 2, 3, 4]가 아닌 [4] !!!

t = int(input())
for test in range(1, t + 1):
    n, m = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]

    max_answer = 1

    for length in range(1, n + 1):
        cost = length ** 2 + (length + 1) ** 2
        for i in range(-length, n - length + 1):
            for j in range(n):
                now_home_cnt = 0

                row, col = i, j
                for k in range(length):
                    if row >= 0:
                        now_home_cnt += sum(area[row][max(0, j - k): j + k + 1])
                    row += 1

                if 0 <= i + length < n:
                    now_home_cnt += sum(area[i + length][max(0, j - length): j + length + 1])

                row, col = i + 2 * length, j
                for k in range(length):
                    if row < n:
                        now_home_cnt += sum(area[row][max(0, j - k): j + k + 1])
                    row -= 1

                if now_home_cnt * m >= cost:
                    max_answer = max(max_answer, now_home_cnt)

    print(f"#{test} {max_answer}")
