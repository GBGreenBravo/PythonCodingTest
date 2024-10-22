# 20241022
# 49:50
# 1 / 1

"""
아래 두 모양의 직각이등변삼각형을 찾는 함수가, 각각 find_points_1()와 find_points_2()

111   1
11   111
1   11111

배열을 시계방향 0/90/180/270도 회전시킨 배열들에서,
위 두 모양의 직각이등변삼각형을 찾으려 한다면, 발견될 수 밖에 없음.

배열 90/180/270도 회전시킨 배열에서 유효한 꼭짓점 찾았다면,
adjust_indexes() 함수 이용해서 회전 전의 좌표로 변환시키기.
"""


def adjust_indexes(indexes, cnt):
    if cnt == 0:
        return indexes

    new_indexes = []
    for y, x in indexes:
        dy, dx = 4.5 - y, 4.5 - x
        new_indexes.append([int(4.5 - dx), int(4.5 + dy)])
    return adjust_indexes(new_indexes, cnt - 1)


def find_points_1(arr):
    copied_arr = [row[:] for row in arr]
    for i in range(9):
        for j in range(9):
            if arr[i][j]:
                length = (9 - arr[i][::-1].index(1)) - arr[i].index(1)

                if not length:
                    return None

                for l in range(length + 1):
                    if i + l == 10:
                        break
                    if sum(copied_arr[i + l][j: j + length + 1 - l]) != length + 1 - l:
                        break
                    for k in range(j, j + length + 1 - l):
                        copied_arr[i + l][k] = 0
                else:
                    if not sum(map(sum, copied_arr)):
                        return [[i, j], [i, j + length], [i + length, j]]

                return None
    return None


def find_points_2(arr):
    copied_arr = [row[:] for row in arr]
    for i in range(9):
        for j in range(1, 9):
            if copied_arr[i][j]:
                copied_arr[i][j] = 0
                length = 1

                while True:
                    if i + length == 10:
                        break
                    left, right = j - length, j + length
                    if left == -1 or right == 10 or not copied_arr[i + length][left] or not copied_arr[i + length][right]:
                        break
                    if sum(copied_arr[i + length][left:right + 1]) != 1 + length * 2:
                        return None
                    for k in range(left, right + 1):
                        copied_arr[i + length][k] = 0
                    length += 1

                length -= 1
                if not length:
                    return None
                if not sum(map(sum, copied_arr)):
                    return [[i, j], [i + length, j - length], [i + length, j + length]]

                return None


area = [[int(inp) for inp in str(input())] for _ in range(10)]
area_90 = [list(row)[::-1] for row in zip(*area)]
area_180 = [list(row)[::-1] for row in zip(*area_90)]
area_270 = [list(row)[::-1] for row in zip(*area_180)]

answers = find_points_1(area) or find_points_2(area)
if not answers:
    answers = find_points_1(area_90) or find_points_2(area_90)
    if answers:
        answers = adjust_indexes(answers, 3)
if not answers:
    answers = find_points_1(area_180) or find_points_2(area_180)
    if answers:
        answers = adjust_indexes(answers, 2)
if not answers:
    answers = find_points_1(area_270) or find_points_2(area_270)
    if answers:
        answers = adjust_indexes(answers, 1)

if not answers:
    print(0)
else:
    for answer in sorted(answers):
        print(answer[0] + 1, answer[1] + 1)
