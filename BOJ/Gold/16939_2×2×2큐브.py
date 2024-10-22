# 20241022
# 28:24
# 1 / 3

# 돌리기 6번에 따른 비교만 해주면 됐음.
# 큐브 한쪽 면을 더 추가한 cube_1/2/3으로 index 설정해 놓고,
# [0][i] == [0][i + 1] == [1][i + 2] == [1][i + 3] 으로 돌렸을 때의 한 면이 같은지 검증했음.

# 큐브 한면만 맞춰도 되는 줄 알아서 1번 틀리고,
# 돌린 쪽만 같은지 점검해서 또 1번 틀렸음.

cube = [None] + list(map(int, input().split()))

cube_1 = ((13, 14, 5, 6, 17, 18, 21, 22, 13, 14),
          (15, 16, 7, 8, 19, 20, 23, 24, 15, 16))
cube_2 = ((2, 4, 6, 8, 10, 12, 23, 21, 2, 4),
          (1, 3, 5, 7, 9, 11, 24, 22, 1, 3))
cube_3 = ((14, 16, 9, 10, 19, 17, 4, 3, 14, 16),
          (13, 15, 11, 12, 20, 18, 2, 1, 13, 15))

possible = False

if cube[1] == cube[2] == cube[3] == cube[4]:
    for i in range(0, 7, 2):
        if not (cube[cube_1[0][i]] == cube[cube_1[0][i + 1]] == cube[cube_1[1][i + 2]] == cube[cube_1[1][i + 3]]):
            break
    else:
        possible = True
    for i in range(0, 7, 2):
        if not (cube[cube_1[1][i]] == cube[cube_1[1][i + 1]] == cube[cube_1[0][i + 2]] == cube[cube_1[0][i + 3]]):
            break
    else:
        possible = True
if cube[13] == cube[14] == cube[15] == cube[16]:
    for i in range(0, 7, 2):
        if not (cube[cube_2[0][i]] == cube[cube_2[0][i + 1]] == cube[cube_2[1][i + 2]] == cube[cube_2[1][i + 3]]):
            break
    else:
        possible = True
    for i in range(0, 7, 2):
        if not (cube[cube_2[1][i]] == cube[cube_2[1][i + 1]] == cube[cube_2[0][i + 2]] == cube[cube_2[0][i + 3]]):
            break
    else:
        possible = True
if cube[5] == cube[6] == cube[7] == cube[8]:
    for i in range(0, 7, 2):
        if not (cube[cube_3[0][i]] == cube[cube_3[0][i + 1]] == cube[cube_3[1][i + 2]] == cube[cube_3[1][i + 3]]):
            break
    else:
        possible = True
    for i in range(0, 7, 2):
        if not (cube[cube_3[1][i]] == cube[cube_3[1][i + 1]] == cube[cube_3[0][i + 2]] == cube[cube_3[0][i + 3]]):
            break
    else:
        possible = True

print(int(possible))
