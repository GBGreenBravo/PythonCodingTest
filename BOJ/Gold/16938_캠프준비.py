# 20240805
# 13:48
# 1 / 1


n, l, r, x = map(int, input().split())
difficulties = list(map(int, input().split()))

difficulties.sort()  # 최소, 최대를 찾기 간편하게 sort()


def get_combination(combi, index):  # n의 길이의 리스트에 대해 2**n개의 조합을 combis에 저장하는 함수
    if index == n:
        combis.append(combi)
        return
    get_combination(combi + [difficulties[index]], index + 1)
    get_combination(combi, index + 1)


combis = []
get_combination([], 0)
combis = [i for i in combis if len(i) >= 2]  # 성적은 최소 2개 이상이어야 하므로 필터링

answer = 0
for combinaiton in combis:
    sm = sum(combinaiton)
    diff = combinaiton[-1] - combinaiton[0]
    if l <= sm <= r and x <= diff:  # 문제가 요구하는 조건에 해당하는 조합이면 += 1
        answer += 1
print(answer)
