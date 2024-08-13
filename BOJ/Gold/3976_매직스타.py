# 20240813
# 45:48
# 1 / 1

"""
1. 문제 분석
-

2. 설계
-

3. 구현
-
"""


def check():  # 현재의 수 조합이 매직스타가 될 수 있는지 체크하는 함수
    num_check_arr = [i for i in origin]  # 현재의 조합에 따른 수를 순서대로 저장할 배열
    for i in range(len_empty):
        num_check_arr[empty[i]] = num_arr[i]

    n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11 = num_check_arr[0], num_check_arr[1], num_check_arr[2], num_check_arr[3], num_check_arr[4], num_check_arr[5], num_check_arr[6], num_check_arr[7], num_check_arr[8], num_check_arr[9], num_check_arr[10], num_check_arr[11]
    # 6개의 26 합 조건을 만족하는지 판단하고, 하나라도 틀리면 return False
    if n1 + n2 + n3 + n4 != 26:
        return False
    if n0 + n2 + n5 + n7 != 26:
        return False
    if n0 + n3 + n6 + n10 != 26:
        return False
    if n7 + n8 + n9 + n10 != 26:
        return False
    if n1 + n5 + n8 + n11 != 26:
        return False
    if n4 + n6 + n9 + n11 != 26:
        return False

    return num_check_arr  # 현재의 수 조합이 매직스타가 된다면 정답배열 return


def dfs(cnt):
    global answer_arr
    if answer_arr:  # 이미 사전순으로 가장 앞에 있는 정답 찾았다면 종료
        return

    if cnt == len_empty:  # 필요한 만큼 숫자조합 채웠다면
        result = check()  # 매직스타 되는지 체크
        if result:  # 매직스타로 판명되어 정답배열 return 했다면
            answer_arr = result  # 정답배열 저장하고 return
            return
        return

    for i in candidates:  # 후보군이 되는 숫자들 중
        if i not in num_arr:  # 중복 없이 선발하고 DFS
            num_arr.append(i)
            dfs(cnt + 1)
            num_arr.pop()


n, m = 5, 9
hexagram = [list(str(input())) for _ in range(5)]
star_points = [(0, 4), (1, 1), (1, 3), (1, 5), (1, 7), (2, 2), (2, 6), (3, 1), (3, 3), (3, 5), (3, 7), (4, 4)]  # 알파벳이 있어야할 좌표들
char_to_num = dict(zip(list('ABCDEFGHIJKL'), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  # 알파벳을 숫자로 변환하는 dictionary
num_to_char = dict(zip(list(char_to_num.values()), list(char_to_num.keys())))  # 숫자를 알파벳으로 변환하는 dictionary

origin = [None] * 12  # 입력돼있는 알파벳을 숫자로 변환하고, star_points의 좌표에 맞는 인덱스에 저장
empty = [True] * 12  # 비어있는 star_points 좌표의 인덱스를 저장할 배열
candidates = list(range(1, 13))  # 필요한 숫자들을 남길 배열

for i in range(n):
    for j in range(m):
        if hexagram[i][j] != '.':
            if hexagram[i][j] != 'x':
                origin[star_points.index((i, j))] = char_to_num[hexagram[i][j]]  # 입력돼 있는 알파벳을 숫자로 바꿔 저장
                empty[star_points.index((i, j))] = False  # 비어 있지 않는 좌표를 체크
                candidates.remove(char_to_num[hexagram[i][j]])  # 이미 존재하여, 후보군이 되지 못하는 숫자 제거

empty = [i for i in range(12) if empty[i]]  # 비어있는 star_points의 좌표 인덱스만을 남김
len_empty = len(empty)

num_arr = []
answer_arr = []
dfs(0)  # 조합에 따른 정답을 answer_arr에 저장

for i in range(n):
    row = ''
    for j in range(m):
        if (i, j) in star_points:
            row += num_to_char[answer_arr[star_points.index((i, j))]]
        else:
            row += '.'
    print(row)
