# 20241130
# 32:16
# 1 / 3

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
# x축 가로지르는 변을 올라가는 방향으로 두 꼭짓점이 가장 앞에 배치될 때까지 위치 재조정
while not(points[0][0] == points[1][0] and points[0][1] < 0 < points[1][1]):
    points.append(points.pop(0))

# x축 가로지르는지 체크하면서 올라갈 때랑 내려갈 때 번호 맞춰주기
arr = []
num = 0
making = False
for i in range(N - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    if x1 == x2 and y1 * y2 < 0:
        arr.append((x1, num))
        if not making:
            making = True
        else:
            making = False
            num += 1

# x기준 오름차순 정렬
arr.sort()

biggest, smallest = 0, 0  # 다른 봉우리에 의해 포함되지 않는 봉우리 개수, 다른 봉우리를 포함하지 않는 봉우리 개수
stk = []
for i in range(len(arr)):
    now = arr[i][1]

    # 스택에 맨 위 값이 now와 같다면 스택에서 제거
    if stk and stk[-1] == now:
        if arr[i - 1][1] == now:  # 바로 이전에 now와 같은 값이 추가됐다면, smallest += 1
            smallest += 1
        stk.pop()
        continue

    # 스택에 추가
    if not stk:  # 스택에 값 없다면, biggest += 1
        biggest += 1
    stk.append(now)

print(biggest, smallest)
