# 20240806
# 21:45
# 1 / 4


def solve(a, b, c):
    if (a + 2 * b + 3 * c) % 2 == 1:  # 총면적 합이 홀수라면 불가능
        return "No"

    while c != 0 and b >= 0 and a > 0:  # c를 먼저 처리해주는 루프; 가장 단순하게 처리해주는 2가지 -> (a, b, c)인 경우와 (a, c)인 경우
        if b % 2 == 1:  # b의 개수가 홀수라면, (a, b, c) 1번 처리해주기.
            c -= 1
            b -= 1
            a -= 1
        else:  # b의 개수가 짝수라면, c와 상관없이 처리 가능. 그러므로 (a, c) c번 처리해주기.
            a -= c
            c = 0

    if c > 0 or a < 0 or b < 0:  # c가 다 처리되지 못하거나, a나 b가 음수일 때
        return "No"

    if (a + 2 * b) % 2 == 1:  # 위 과정을 거치고 남은, a와 b의 합이 홀수인 경우.
        return "No"

    if a == 0 and b % 2 == 1:  # 위 과정을 거치고 남은 게, 0/1/0 인 경우 (b블록 회전 불가능하기 때문)
        return "No"

    return "Yes"


t = int(input())
for _ in range(t):
    aa, bb, cc = map(int, input().split())
    print(solve(aa, bb, cc))
