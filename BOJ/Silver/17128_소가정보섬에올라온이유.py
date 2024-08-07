# 20240807
# 19:52
# 1 / 1

n, q = map(int, input().split())
qualities = list(map(int, input().split()))
funs = list(map(int, input().split()))

qualities.extend(qualities[:3])  # s를 계산해주기 위해, 0,1,2 인덱스 값 임의로 추가

multiplies = [0] * n  # index번호에서 시작하는 '4개 연속의 곱' 저장
for i in range(n):
    multiplying = 1
    for j in range(4):
        multiplying *= qualities[i + j]
    multiplies[i] = multiplying
s = sum(multiplies)  # 초기 s를 저장

for fun_index in funs:  # 장난칠 index
    change_to_s = 0  # 장난으로 인해 s에 반영될 변화량 선언
    for i in range(4):
        now_index = fun_index - 4 + i  # 현재i-3 ~ 현재i 인덱스
        multiplies[now_index] *= -1  # 장난 반영
        change_to_s += multiplies[now_index] * 2  # 변화량 추가
    s += change_to_s  # 장난에 따른 총 변화량 반영
    print(s)
