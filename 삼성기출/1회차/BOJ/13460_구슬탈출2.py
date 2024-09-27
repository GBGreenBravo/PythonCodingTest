# 20240903
# 27:00
# 1 / 1

"""
풀이 시간: 27분 (15:26 ~ 15:53)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:26 - 15:33)
    문제를 읽으며, 두 구슬이 이미 굴러졌던 위치로 다시 동시에 돌아오는 경우를 체크하며
    가지치기를 해줘야 하는지에 대해 생각했습니다.
    그러나 구상한 DFS의 시간복잡도는 4**10 * 2*10 이었기에,
    위의 가지치기 없이도, 시간초과는 발생하지 않을 것으로 생각했습니다.

    문제를 읽으며
    1) 구슬이 단위시간에 1칸씩 이동하며, 단위시간 동안만 기울이는 것인지
    2) 구슬이 끝까지 굴러갈 때까지 기울이는 것인지
    헷갈렸습니다.
    그에 대한 정답은, '기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지'라는 문제 지문에 있었지만,
    인내하지 못하고 테스트케이스를 통해 확인한 점에 성찰할 부분이 있었습니다.


2. 구현 (15:33 - 15:48)
    일단 4방향에 대해 4**10의 조합을 구성해주고, 기울이기를 수행할까도 생각해봤지만,
    앞에서 구멍에 빠지거나 유효하지 않은 동작에 대한 기울이기 수행이 상당 부분 겹칠 것으로 생각하여,
    기울이기를 중간중간에 해준 다음, 유효하지 않은 경우에 가지치기를 하는 것이 효율적일 것이라고 판단했습니다.

    두 구슬을 기울이는 방향으로 굴려주면서, 이동한 좌표들을 기록하면
    문제에서 요구하는 조건들을 처리해줄 수 있다고 생각했고, 생각대로 구현했습니다.


3. 검증 (15:48 - 15:53)
    테스트케이스에서는 모두 다 정상적인 출력을 확인할 수 있었지만,
    메모를 다시보고 검증하는 과정에서,
    빨간 구슬만 구르거나 파란 구슬만 구르는 경우에도, 두 구슬의 좌표가 겹칠 수 있음을 발견했습니다.
    따라서 이에 대한 기존 코드의 허점을 확인하고, 구슬 겹칠 때 한 구슬의 좌표를 복구하는 코드를 추가했습니다.
"""

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


# 이전에 tilted_cnt만큼 굴렸고, 빨간 구슬 좌표(ry, rx)와 파란 구슬 좌표(by, bx)를 받아 direction_idx의 방향으로 기울이는 함수
def tilt(tilted_cnt, ry, rx, by, bx, direction_idx):
    global answer

    if tilted_cnt == 10:  # 이미 10회 기울였다면, return
        return

    dy, dx = direction[direction_idx]  # 구슬들이 굴러갈 방향

    red_rolled = []  # 빨간 구슬이 구르게 될 좌표 배열
    blue_rolled = []  # 파란 구슬이 구르게 될 좌표 배열

    # 빨간 구슬 굴리기
    ry, rx = ry + dy, rx + dx
    while area[ry][rx] in ['.', 'O']:  # 빨간 구슬의 좌표가 유효한 영역일 동안
        red_rolled.append((ry, rx))  # 구르게 될 좌표 배열에 추가
        ry, rx = ry + dy, rx + dx
    ry, rx = ry - dy, rx - dx  # 유효한 좌표로 1칸 복구 (=> 빨간 구슬이 다 구른 후의 좌표)

    # 파란 구슬에 대해서도, 위와 같은 코드로 굴리기
    by, bx = by + dy, bx + dx
    while area[by][bx] in ['.', 'O']:
        blue_rolled.append((by, bx))
        by, bx = by + dy, bx + dx
    by, bx = by - dy, bx - dx

    # 두 구슬 다 구르지 않았다면, return
    if not red_rolled and not blue_rolled:
        return

    # 빨간 구슬만 굴렀다면
    elif red_rolled and not blue_rolled:
        # 두 구슬의 좌표가 겹친다면, 빨간 구슬을 1칸 복구
        if ry == by and rx == bx:
            ry, rx = ry - dy, rx - dx

        # 빨간 구슬이 구른 좌표 배열에 구멍이 있었다면, 최소값 갱신하고 return
        if hole in red_rolled:
            answer = min(answer, tilted_cnt + 1)
            return
        # 빨간 구슬이 구른 좌표 배열에 구멍 없었다면
        else:
            for di in range(4):  # 다음 기울이기 수행 (재귀 호출)
                tilt(tilted_cnt + 1, ry, rx, by, bx, di)

    # 파란 구슬만 굴렀다면
    elif not red_rolled and blue_rolled:
        # 두 구슬의 좌표가 겹친다면, 파란 구슬을 1칸 복구
        if ry == by and rx == bx:
            by, bx = by - dy, bx - dx

        # 파란 구슬이 구른 좌표 배열에 구멍이 있었다면, return
        if hole in blue_rolled:
            return
        # 파란 구슬이 구른 좌표 배열에 구멍 없었다면
        else:
            for di in range(4):  # 다음 기울이기 수행 (재귀 호출)
                tilt(tilted_cnt + 1, ry, rx, by, bx, di)
    else:
        # 두 구슬의 좌표가 겹친다면, 더 많이 구른 구슬을 1칸 복구
        if ry == by and rx == bx:
            if len(red_rolled) < len(blue_rolled):
                by, bx = by - dy, bx - dx
            else:
                ry, rx = ry - dy, rx - dx

        # 파란 구슬이 구른 좌표 배열에 구멍이 있었다면, return (두 구슬 동시에 구멍 빠진 경우도 여기 포함됨)
        if hole in blue_rolled:
            return
        # 빨간 구슬이 구른 좌표 배열에만 구멍이 있었다면, 최소값 갱신하고 return
        elif hole in red_rolled:
            answer = min(answer, tilted_cnt + 1)
            return
        # 두 구슬이 구른 좌표 배열에 구멍 없었다면
        else:
            for di in range(4):  # 다음 기울이기 수행 (재귀 호출)
                tilt(tilted_cnt + 1, ry, rx, by, bx, di)


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

# 빨간 구슬 / 파란 구슬 / 구멍 => 좌표 탐색으로 찾기
for i in range(n):
    for j in range(m):
        if area[i][j] == 'R':
            area[i][j] = '.'  # 구슬 굴러갈 수 있는 칸으로 변경
            red = (i, j)
        elif area[i][j] == 'B':
            area[i][j] = '.'  # 구슬 굴러갈 수 있는 칸으로 변경
            blue = (i, j)
        elif area[i][j] == 'O':
            hole = (i, j)

answer = 11
for i in range(4):  # DFS 함수 초기 호출
    tilt(0, *red, *blue, i)
print(-1 if answer == 11 else answer)
