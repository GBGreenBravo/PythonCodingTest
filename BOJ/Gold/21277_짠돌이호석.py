# 20241025
# 46:15
# 1 / 3

"""
1 1
1
1 3
101

위 테케와 같이,
뒤에 들어오는 배열을 cal_min_answer()의 전자 인자로 넣어줘야 하는 경우 생각 못해서 틀림.

1 3
111
3 1
1
0
1

그리고 위 테케에서,
초기값 설정을 min((n1 + n2) * max(m1, m2), (m1 + m2) * max(n1, n2))로 했기에 틀림.
"""


def cal_min_answer(arr1, arr2):
    global min_answer

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            now_answer = max(len(arr1), i + len(arr2)) * max(len(arr1[0]), j + len(arr2[0]))
            if now_answer >= min_answer:
                continue

            possible = True
            for dy in range(len(arr2)):
                for dx in range(len(arr2[0])):
                    if len(arr1) <= i + dy or len(arr1[0]) <= j + dx:
                        continue
                    if arr1[i + dy][j + dx] and arr2[dy][dx]:
                        possible = False
                        break
                else:
                    continue
                break

            if possible:
                min_answer = now_answer


n1, m1 = map(int, input().split())
area1_0 = [[int(inp) for inp in str(input())] for _ in range(n1)]
area1_90 = [list(row)[::-1] for row in zip(*area1_0)]
area1_180 = [list(row)[::-1] for row in zip(*area1_90)]
area1_270 = [list(row)[::-1] for row in zip(*area1_180)]
n2, m2 = map(int, input().split())
area2_0 = [[int(inp) for inp in str(input())] for _ in range(n2)]
area2_90 = [list(row)[::-1] for row in zip(*area2_0)]
area2_180 = [list(row)[::-1] for row in zip(*area2_90)]
area2_270 = [list(row)[::-1] for row in zip(*area2_180)]

min_answer = min(
    (n1 + n2) * max(m1, m2),
    (m1 + m2) * max(n1, n2),
    (n1 + m2) * max(n2, m1),
    (n2 + m1) * max(n1, m2)
)

cal_min_answer(area1_0, area2_0)
cal_min_answer(area1_0, area2_90)
cal_min_answer(area1_0, area2_180)
cal_min_answer(area1_0, area2_270)
cal_min_answer(area1_90, area2_0)
cal_min_answer(area1_90, area2_90)
cal_min_answer(area1_90, area2_180)
cal_min_answer(area1_90, area2_270)
cal_min_answer(area1_180, area2_0)
cal_min_answer(area1_180, area2_90)
cal_min_answer(area1_180, area2_180)
cal_min_answer(area1_180, area2_270)
cal_min_answer(area1_270, area2_0)
cal_min_answer(area1_270, area2_90)
cal_min_answer(area1_270, area2_180)
cal_min_answer(area1_270, area2_270)

cal_min_answer(area2_0, area1_0)
cal_min_answer(area2_90, area1_0)
cal_min_answer(area2_180, area1_0)
cal_min_answer(area2_270, area1_0)
cal_min_answer(area2_0, area1_90)
cal_min_answer(area2_90, area1_90)
cal_min_answer(area2_180, area1_90)
cal_min_answer(area2_270, area1_90)
cal_min_answer(area2_0, area1_180)
cal_min_answer(area2_90, area1_180)
cal_min_answer(area2_180, area1_180)
cal_min_answer(area2_270, area1_180)
cal_min_answer(area2_0, area1_270)
cal_min_answer(area2_90, area1_270)
cal_min_answer(area2_180, area1_270)
cal_min_answer(area2_270, area1_270)

print(min_answer)


# 로직은 같으나, 간결하게 정리한 코드
"""
def cal_min_answer(arr1, arr2):
    global min_answer

    for y in range(len(arr1)):
        for x in range(len(arr1[0])):
            now_answer = max(len(arr1), y + len(arr2)) * max(len(arr1[0]), x + len(arr2[0]))
            if now_answer >= min_answer:
                continue

            possible = True
            for dy in range(len(arr2)):
                for dx in range(len(arr2[0])):
                    if len(arr1) <= y + dy or len(arr1[0]) <= x + dx:
                        continue
                    if arr1[y + dy][x + dx] and arr2[dy][dx]:
                        possible = False
                        break
                else:
                    continue
                break

            if possible:
                min_answer = now_answer


n1, m1 = map(int, input().split())
area_1 = [[[int(inp) for inp in str(input())] for _ in range(n1)]]
for _ in range(3):
    area_1.append([list(row)[::-1] for row in zip(*area_1[-1])])
n2, m2 = map(int, input().split())
area_2 = [[[int(inp) for inp in str(input())] for _ in range(n2)]]
for _ in range(3):
    area_2.append([list(row)[::-1] for row in zip(*area_2[-1])])

min_answer = min(
    (n1 + n2) * max(m1, m2),
    (m1 + m2) * max(n1, n2),
    (n1 + m2) * max(n2, m1),
    (n2 + m1) * max(n1, m2))
for i in range(4):
    for j in range(4):
        cal_min_answer(area_1[i], area_2[j])
        cal_min_answer(area_2[j], area_1[i])
print(min_answer)
"""
