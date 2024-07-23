# 20240723
# 31:09

# ground를 2차원 리스트로 받을 필요 없음.
# 1차원 리스트로 받고, 내림차순 정렬.
#
# make_flat() 함수 ; ground_1, height, inven_block을 받아 -> 소요시간과 남은 블럭수를 반환한다.
#   내림차순 정렬된 ground_1을 탐색하며,
#       1) 현재 땅보다 height가 더 높고 and 인벤블록이 그만큼보다 더 남으면 -> 인벤블럭, 시간 소모
#       2) 현재 땅보다 height가 더 높고 and 인벤블록이 그만큼보다 없으면 -> height만큼 평탄화 불가 / False를 return
#       3) 현재 땅보다 height가 더 낮다면 -> 시간 소모, 인벤블럭 저장
#
# h(height)를 평탄화할 수 있는 최대의 높이로 설정.
# while문
#   현재의 h를 위해 소모된 시간과 남은블럭을 second, remain으로 저장.
#   1) second가 0이면 -> 이미 평탄화돼있는 것이므로 그대로.
#   2) second가 False면 -> 불가능한 높이이므로, h -= 1
#   3) second가 0보다 크고 and result_second보다 작다면 -> 더 효율적인 높이이므로 result 갱신, h -= 1
#   4) second가 0보다 크고 result_second보다 크다면 -> 이전 높이(+1)의 소요시간보다 더 소모된다는 건 비효율적인 뜻이므로, break

n, m, b = map(int, input().split())

ground = []
for _ in range(n):
    ground.extend(map(int, input().split()))
ground.sort(reverse=True)


def make_flat(ground_1, height, inven_blocks):
    sec = 0
    for i in ground_1:
        if i < height and height - i <= inven_blocks:
            inven_blocks -= height - i
            sec += height - i
        elif i < height and height - i > inven_blocks:
            return False, False
        elif i >= height:
            sec += 2 * (i - height)
            inven_blocks += i - height
    return sec, inven_blocks


h = (sum(ground) + b) // (m * n)
result_second = sum(ground) * 2 + b
result_height = h
while True:
    second, remain = make_flat(ground, h, b)
    if second == 0:
        result_second = second
        result_height = h
        break
    elif not second:
        h -= 1
    elif second < result_second:
        result_second = second
        result_height = h
        h -= 1
    else:
        break

print(result_second, result_height)


# 높이 구간이 0에서 256으로 설정돼 있으므로 더 간편하게 구할 수 있음. 정렬을 안 해서, 시간은 더 소모됨.
"""
n, m, b = map(int, input().split())
ground = []
for _ in range(n):
    ground.extend(map(int, input().split()))

result_second = sum(ground) * 2 + b
result_height = 256
for height in range(256, -1, -1):
    second, remain = 0, b
    for g in ground:
        if g > height:
            remain += g - height
            second += 2 * (g - height)
        elif g < height:
            remain -= height - g
            second += 1 * (height - g)
    if remain < 0:
        continue
    elif second < result_second:
        result_second, result_height = second, height

print(result_second, result_height)
"""