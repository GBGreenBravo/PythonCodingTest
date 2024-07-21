# 20240721
# 23:10

# left, right로 사각형의 가로를 비교 -> 겹치는 부분이 없으면 3 / 한 점에서 만나면 2 / 겹치면 1
# down, up으로 사각형의 가로도 같은 방식으로 비교
# 위 비교 결과로, 답변 도출 가능
#     가로 세로 중, 하나라도 겹치지 않으면(3) -> d (겹치지 않는 사각형)
#     가로 세로 모두 한 점에서 만나면(2) -> c (한 점에서 만나는 사각형)
#     가로 세로 모두 겹치면(1) -> a (겹치는 사각형)
#     기타의 경우(1and2) -> b (선으로 만나는 사각형)

for _ in range(4):
    rectangles = list(map(int, input().split()))

    result = tuple()

    left = (rectangles[0], rectangles[2])
    right = (rectangles[4], rectangles[6])
    if rectangles[4] < rectangles[0]: # or (rectangles[0] == rectangles[4] and rectangles[6] < rectangles[2]) 시작점 같으면 어느쪽이 left/right 돼도 비교 결과에 영향 없으므로 생략 가능.
        left, right = right, left

    if left[1] < right[0]:
        result += 3,
    elif left[1] == right[0]:
        result += 2,
    else:
        result += 1,

    down = (rectangles[1], rectangles[3])
    up = (rectangles[5], rectangles[7])
    if rectangles[5] < rectangles[1]:
        down, up = up, down

    if down[1] < up[0]:
        result += 3,
    elif down[1] == up[0]:
        result += 2,
    else:
        result += 1,

    if 3 in result:
        print('d')
    elif result[0] == 2 and result[1] == 2:
        print('c')
    elif result[0] == 1 and result[1] == 1:
        print('a')
    else:
        print('b')
