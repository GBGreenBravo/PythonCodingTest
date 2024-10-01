# 20240930
# 18:56
# 1 / 2

# 15684_사다리조작

"""
풀이 시간: 19분 (15:37 - 15:56)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (15:37 - 15:44)


2. 구현 (15:44 - 15:52)
    이전 풀이방식과 거의 유사했습니다.
    이전에는 함수화를 더 잘게 했던 것 같은데, 이는 문제유형/풀이시간에 따른 차이로 보입니다.


3. 디버깅 (-)


4. 런타임에러 (15:52 - 15:56)
    사다리 내려가는 check함수의 while문에서 종료조건이
    height < h - 1 가 아닌 height < n 으로 적혀있었습니다.
    초기값 설정과 그에 따른 종료조건 체크 & 인덱스에러 주의 를 더욱 인지해야겠습니다.
"""


def check():
    for idx in range(n):
        col = idx
        height = -1
        while height < h - 1:
            height += 1
            col += connected[height][col]
        if col != idx:
            return False

    return True


def dfs(cnt, start_idx):
    global possible

    if possible:
        return

    if cnt == additional:
        if check():
            possible = True
        return

    for idx in range(start_idx, len_candidates):
        ay, ax = candidates[idx]
        by, bx = ay, ax + 1
        if not connected[ay][ax] and not connected[by][bx]:
            connected[ay][ax] = 1
            connected[by][bx] = -1
            dfs(cnt + 1, idx + 1)
            connected[ay][ax] = 0
            connected[by][bx] = 0


n, m, h = map(int, input().split())
connected = [[0] * n for _ in range(h)]
for _ in range(m):
    aa, bb = map(lambda inp: int(inp) - 1, input().split())
    connected[aa][bb] = 1
    connected[aa][bb + 1] = -1

candidates = []
for i in range(h):
    for j in range(n - 1):
        if not connected[i][j] and not connected[i][j + 1]:
            candidates.append((i, j))
len_candidates = len(candidates)

for additional in range(4):
    possible = False

    dfs(0, 0)

    if possible:
        print(additional)
        break
else:
    print(-1)
