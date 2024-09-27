# 20240912
# 1:13:00
# 1 / 1

"""
풀이 시간: 1시간 13분 (14:58 ~ 16:11)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:58 - 15:12)
    문제 지문이 길다고 생각했지만, 그림과 함께 친절하게 설명돼있었기 때문에,
    문제 이해는 단번에 할 수 있었습니다.

    문제를 읽으며 궁금했던 부분:
    블리자드 마법에서 얼음파편으로 구슬 파괴할 때, 영역 바깥까지 공격이 가능한지 (가능하다면 oob 처리를 따로 해줘야 하기 때문)
    => 문제의 제한 조건에서 si ≤ (N-1)/2 를 확인했기에, 메모에서 X처리로 지웠습니다.

    메모에서 반복작업을 명확하게 표시하기 위해,
    마법 1회에 따른 반복작업을 네모 박스로 묶어서 표시했습니다.

    "1913_달팽이", "20057_마법사 상어와 토네이도" 문제와 마찬가지로,
    홀수인 N의 N*N 배열에서, 소용돌이 모양으로 문제를 풀어야 했습니다.
    이제까지 풀어왔던 방식대로,
    바깥부터 좌표를 탐색하는 방식을 택하기로 했습니다.

    구슬을 저장하는데 있어서는, 굴리기 처리를 별도로 할 필요 없이,
    0이 아닌 1/2/3 만 구슬 배열로 저장하기로 생각했습니다.


2. 구현 (15:12 - 16:00)
    반복적이고 독립적인 작업을 수행한다고 생각했기에,
    이번에도 메인코드 먼저 작성하고, 독립적인 작업은 함수명으로만 표시했습니다.
    1) destroy(): 얼음파편으로 특정 방향/거리의 구슬을 파괴하고, 구슬 굴리는 함수
    2) explode(): 4개 이상 연속하는 구슬 폭발시키고, 구슬 굴리는 함수
    3) convert(): 연속 그룹별로 구슬 변화시키는 함수

    destroy()함수를 구현하기에 앞서,
    상하좌우별로 얼음파편 거리에 따른 구슬 배열 index는 고정이기에,
    해당 테이블을 저장해놓고 활용하면 좋겠다고 생각했습니다.
    따라서, 해당 값을 destroyed_marble_indexes에 저장해뒀습니다.


3. 검증 (16:00 - 16:11)
    에러가 터졌을 때 의심되는 부분에서 이상 발견 못했으면,
    코드만 보고있지 말고, print()든 디버그모드든 가시성 있는 방식으로 디버깅하자.

    구슬의 연쇄 폭발 때문에, 시간복잡도 체크 어려웠음.

"""

from collections import deque

direction_clockwise = ((0, 1), (1, 0), (0, -1), (-1, 0))
direction = (None, (-1, 0), (1, 0), (0, -1), (0, 1))


def destroy():
    global marbles

    soon_destroyed = destroyed_marble_indexes[blizzard_d][1: blizzard_s + 1]
    new_marbles = deque()
    for m_idx in range(len(marbles)):
        if m_idx in soon_destroyed:
            continue
        new_marbles.append(marbles[m_idx])
    marbles = new_marbles


def explode():
    global marbles

    if not marbles:
        return False

    exploded_flag = False

    tmp = [[marbles.popleft()]]
    while marbles:
        popped_marble = marbles.popleft()
        if popped_marble == tmp[-1][-1]:
            tmp[-1].append(popped_marble)
        else:
            tmp.append([popped_marble])

    new_marbles = deque()
    for t in tmp:
        if len(t) >= 4:
            exploded_flag = True
            exploded_cnt_arr[t[0]] += len(t)
            continue
        new_marbles.extend(t)
    marbles = new_marbles

    return exploded_flag


def convert():
    global marbles

    if not marbles:
        return False

    tmp = [[marbles.popleft()]]
    while marbles:
        popped_marble = marbles.popleft()
        if popped_marble == tmp[-1][-1]:
            tmp[-1].append(popped_marble)
        else:
            tmp.append([popped_marble])

    new_marbles = deque()
    for t in tmp:
        new_marbles.append(len(t))
        new_marbles.append(t[0])

    marbles = deque(list(new_marbles)[:n**2 - 1])
    return


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

marble_num_by_index = [[0] * n for _ in range(n)]
now_num = 0

my, mx, md = 0, 0, 0
marbles = deque([area[my][mx]]) if area[my][mx] else deque()
marble_visited = [[0] * n for _ in range(n)]
marble_visited[0][0] = 1
while my != n // 2 or mx != n // 2:
    mdy, mdx = direction_clockwise[md]
    mny, mnx = my + mdy, mx + mdx
    if mny < 0 or n <= mny or mnx < 0 or n <= mnx or marble_visited[mny][mnx]:
        md = (md + 1) % 4
        mdy, mdx = direction_clockwise[md]
        mny, mnx = my + mdy, mx + mdx
    marble_visited[mny][mnx] = 1
    if area[mny][mnx]:
        marbles.append(area[mny][mnx])
    my, mx = mny, mnx

    now_num += 1
    marble_num_by_index[my][mx] = now_num
marbles.reverse()

destroyed_marble_indexes = [None, [None], [None], [None], [None]]
y1, x1, y2, x2, y3, x3, y4, x4 = n // 2, n // 2, n // 2, n // 2, n // 2, n // 2, n // 2, n // 2
for i in range(n // 2):
    y1, x1 = y1 + direction[1][0], x1 + direction[1][1]
    destroyed_marble_indexes[1].append(n**2 - 2 - marble_num_by_index[y1][x1])
    y2, x2 = y2 + direction[2][0], x2 + direction[2][1]
    destroyed_marble_indexes[2].append(n**2 - 2 - marble_num_by_index[y2][x2])
    y3, x3 = y3 + direction[3][0], x3 + direction[3][1]
    destroyed_marble_indexes[3].append(n**2 - 2 - marble_num_by_index[y3][x3])
    y4, x4 = y4 + direction[4][0], x4 + direction[4][1]
    destroyed_marble_indexes[4].append(n**2 - 2 - marble_num_by_index[y4][x4])

exploded_cnt_arr = [0, 0, 0, 0]

for _ in range(m):
    blizzard_d, blizzard_s = map(int, input().split())
    destroy()
    while True:
        if not explode():
            break
    convert()

answer = 0
for i in range(1, 4):
    answer += i * exploded_cnt_arr[i]
print(answer)
