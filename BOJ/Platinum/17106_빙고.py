# 20241201
# 47:29
# 1 / 1

"""
정답은 아래와 같다.
.#..#
#####
..#.#
.##.#
#..##
"""


def cal_bingo_lines():
    lines = []
    if sum([dfs_arr[0], dfs_arr[1], dfs_arr[2], dfs_arr[3], dfs_arr[4]]) == 5:
        lines.append('1')
    if sum([dfs_arr[5], dfs_arr[6], dfs_arr[7], dfs_arr[8], dfs_arr[9]]) == 5:
        lines.append('2')
    if sum([dfs_arr[10], dfs_arr[11], dfs_arr[12], dfs_arr[13], dfs_arr[14]]) == 5:
        lines.append('3')
    if sum([dfs_arr[15], dfs_arr[16], dfs_arr[17], dfs_arr[18], dfs_arr[19]]) == 5:
        lines.append('4')
    if sum([dfs_arr[20], dfs_arr[21], dfs_arr[22], dfs_arr[23], dfs_arr[24]]) == 5:
        lines.append('5')

    if sum([dfs_arr[0], dfs_arr[5], dfs_arr[10], dfs_arr[15], dfs_arr[20]]) == 5:
        lines.append('A')
    if sum([dfs_arr[1], dfs_arr[6], dfs_arr[11], dfs_arr[16], dfs_arr[21]]) == 5:
        lines.append('B')
    if sum([dfs_arr[2], dfs_arr[7], dfs_arr[12], dfs_arr[17], dfs_arr[22]]) == 5:
        lines.append('C')
    if sum([dfs_arr[3], dfs_arr[8], dfs_arr[13], dfs_arr[18], dfs_arr[23]]) == 5:
        lines.append('D')
    if sum([dfs_arr[4], dfs_arr[9], dfs_arr[14], dfs_arr[19], dfs_arr[24]]) == 5:
        lines.append('E')

    if sum([dfs_arr[0], dfs_arr[6], dfs_arr[12], dfs_arr[18], dfs_arr[24]]) == 5:
        lines.append('A1')
    if sum([dfs_arr[4], dfs_arr[8], dfs_arr[12], dfs_arr[16], dfs_arr[20]]) == 5:
        lines.append('E1')

    return lines


def cal_bingo_parts(lines):
    cnt = 0
    if dfs_arr[0] and ('A' in lines or '1' in lines or 'A1' in lines):
        cnt += 1
    if dfs_arr[1] and ('B' in lines or '1' in lines):
        cnt += 1
    if dfs_arr[2] and ('C' in lines or '1' in lines):
        cnt += 1
    if dfs_arr[3] and ('D' in lines or '1' in lines):
        cnt += 1
    if dfs_arr[4] and ('E' in lines or '1' in lines or 'E1' in lines):
        cnt += 1

    if dfs_arr[5] and ('A' in lines or '2' in lines):
        cnt += 1
    if dfs_arr[6] and ('B' in lines or '2' in lines or 'A1' in lines):
        cnt += 1
    if dfs_arr[7] and ('C' in lines or '2' in lines):
        cnt += 1
    if dfs_arr[8] and ('D' in lines or '2' in lines or 'E1' in lines):
        cnt += 1
    if dfs_arr[9] and ('E' in lines or '2' in lines):
        cnt += 1

    if dfs_arr[10] and ('A' in lines or '3' in lines):
        cnt += 1
    if dfs_arr[11] and ('B' in lines or '3' in lines):
        cnt += 1
    if dfs_arr[12] and ('C' in lines or '3' in lines or 'A1' in lines or 'E1' in lines):
        cnt += 1
    if dfs_arr[13] and ('D' in lines or '3' in lines):
        cnt += 1
    if dfs_arr[14] and ('E' in lines or '3' in lines):
        cnt += 1

    if dfs_arr[15] and ('A' in lines or '4' in lines):
        cnt += 1
    if dfs_arr[16] and ('B' in lines or '4' in lines or 'E1' in lines):
        cnt += 1
    if dfs_arr[17] and ('C' in lines or '4' in lines):
        cnt += 1
    if dfs_arr[18] and ('D' in lines or '4' in lines or 'A1' in lines):
        cnt += 1
    if dfs_arr[19] and ('E' in lines or '4' in lines):
        cnt += 1

    if dfs_arr[20] and ('A' in lines or '5' in lines or 'E1' in lines):
        cnt += 1
    if dfs_arr[21] and ('B' in lines or '5' in lines):
        cnt += 1
    if dfs_arr[22] and ('C' in lines or '5' in lines):
        cnt += 1
    if dfs_arr[23] and ('D' in lines or '5' in lines):
        cnt += 1
    if dfs_arr[24] and ('E' in lines or '5' in lines or 'A1' in lines):
        cnt += 1

    return cnt


def check():
    lines = cal_bingo_lines()
    bingo_parts_cnt = cal_bingo_parts(lines)
    not_bingo_parts_cnt = sum(dfs_arr) - bingo_parts_cnt

    if dfs_arr[0] is True:
        if 'E1' in lines:
            return False
    else:
        if 'E1' not in lines:
            return False

    if dfs_arr[1] is True:
        if '1' in lines or 'B' in lines:
            return False
    else:
        return False

    if dfs_arr[2] is True:
        if 'A1' not in lines:
            return False
    else:
        if 'A1' in lines:
            return False

    if dfs_arr[3] is True:
        if dfs_arr[18] is False:
            return False
    else:
        if dfs_arr[18] is True:
            return False

    if dfs_arr[4] is True:
        if '1' not in lines and 'E' not in lines and 'E1' not in lines:
            return False
    else:
        pass

    if dfs_arr[5] is True:
        if dfs_arr[15] is True:
            return False
    else:
        if dfs_arr[15] is False:
            return False

    lines_set = set(lines)
    if dfs_arr[6] is True:
        if not ({'1', '2', '3', '4', '5'} & lines_set and {'A', 'B', 'C', 'D', 'E'} & lines_set and {'A1', 'E1'} & lines_set):
            return False
    else:
        if {'1', '2', '3', '4', '5'} & lines_set and {'A', 'B', 'C', 'D', 'E'} & lines_set and {'A1', 'E1'} & lines_set:
            return False

    # 7은 뭐든 ok

    if dfs_arr[8] is True:
        if sum(dfs_arr) > 17:
            return False
    else:
        if sum(dfs_arr) <= 17:
            return False

    if dfs_arr[9] is True:
        if bingo_parts_cnt % 2 == 1:
            return False
    else:
        if bingo_parts_cnt % 2 == 0:
            return False

    if dfs_arr[10] is True:
        if 'A' not in lines and '3' not in lines:
            return False
    else:
        pass

    if dfs_arr[11] is True:
        if not_bingo_parts_cnt < 5:
            return False
    else:
        if not_bingo_parts_cnt >= 5:
            return False

    if dfs_arr[12] is True:
        if 'C' not in lines and '3' not in lines and 'A1' not in lines and 'E1' not in lines:
            return False

    if dfs_arr[13] is True:
        if len({'A', 'B', 'C', 'D', 'E'} & lines_set) < 2:
            return False
    else:
        if len({'A', 'B', 'C', 'D', 'E'} & lines_set) >= 2:
            return False

    if dfs_arr[14] is True:
        if 25 - bingo_parts_cnt < 10:
            return False
    else:
        if 25 - bingo_parts_cnt >= 10:
            return False

    if dfs_arr[15] is True:
        if dfs_arr[5] is True:
            return False
    else:
        if dfs_arr[5] is False:
            return False

    if dfs_arr[16] is True:
        if '2' not in lines and 'D' not in lines:
            return False
    else:
        if '2' in lines or 'D' in lines:
            return False

    if dfs_arr[17] is True:
        if sum([dfs_arr[2], dfs_arr[7], dfs_arr[12], dfs_arr[17], dfs_arr[22]]) > 3:
            return False
    else:
        if sum([dfs_arr[2], dfs_arr[7], dfs_arr[12], dfs_arr[17], dfs_arr[22]]) <= 3:
            return False

    if dfs_arr[18] is True:
        if dfs_arr[3] is False:
            return False
    else:
        if dfs_arr[3] is True:
            return False

    if dfs_arr[19] is True:
        if 'A1' not in lines and 'E1' not in lines:
            return False
    else:
        if 'A1' in lines or 'E1' in lines:
            return False

    if dfs_arr[20] is True:
        if dfs_arr[24] is False:
            return False
    else:
        if dfs_arr[24] is True:
            return False

    # 21이 참일 때 1개 + 거짓일 때 1개로, 참이려면 1개로 틀리기에, 거짓임.

    # 22는 뭐든 ok

    if dfs_arr[23] is True:
        if len(lines) < 3:
            return False
    else:
        if len(lines) >= 3:
            return False

    if dfs_arr[24] is True:
        if dfs_arr[20] is False:
            return False
    else:
        if dfs_arr[20] is True:
            return False

    return True


def dfs(cnt):
    if cnt == 25:
        if check():
            print(dfs_arr)
        return

    if cnt in (12,):
        dfs_arr.append(True)
        dfs(cnt + 1)
        dfs_arr.pop()
        return

    if cnt in (21,):
        dfs_arr.append(False)
        dfs(cnt + 1)
        dfs_arr.pop()
        return

    dfs_arr.append(True)
    dfs(cnt + 1)
    dfs_arr[-1] = False
    dfs(cnt + 1)
    dfs_arr.pop()


dfs_arr = []
dfs(0)
