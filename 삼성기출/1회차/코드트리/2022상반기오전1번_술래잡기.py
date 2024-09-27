# 20240919
# 1:36:00
# 1 / 1

"""
풀이 시간: 1시간 36분 (14:10 ~ 15:46)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:10 - 14:26)
    오전의 '예술성' 문제에서 정독&구상 단계가 6분만에 너무 빨리 끝났다고 회고했기에,
    이번 문제에서는 더 천천히&꼼꼼히 문제를 정독&메모 했습니다.

    도망자의 이동은 N*N배열의 각 좌표에 리스트를 선언해주고, 각 도망자의 방향만을 넣어주면 되는 것으로 구상했습니다.

    술래의 이동은 나선형 회전이지만, 같은 루트를 왔다갔다 하고 갈때의 방향과 올때의 방향이 달라지기에,
    갈때의 방향과 올때의 방향을 달리 해주면 될 것으로 생각했습니다.
    N이 홀수였기에, (0, 0)에서 아래로 나선형 회전하는 것으로 구상했습니다.


2. 구현 (14:26 - 15:00)
    술래의 나선형 이동루트와 그에 따른 각 방향을 먼저 구현했습니다.
    구현이 끝나고 난 뒤, 체크포인트로써
    갈때와 올때의 방향을 5*5배열에서 체크했습니다.

    도망자와 술래의 이동을 구현한 뒤, 체크포인트로 중간검증했다면 좋았겠지만,
    마땅한 체크포인트를 찾지 못해, (검증 1단계를 자세히 해줄 것으로 생각하고)
    구현 후 바로 테케를 돌려봤습니다.


3. 디버깅 (X)
    테스트케이스 실행에서 아무런 에러가 발생하지 않았기 때문에
    디버깅을 수행할 필요가 없었습니다.


4. 검증 (15:00 - 15:46)
    결론부터 적어보자면,
    15시 38분경, 검증루틴 4단계(커스텀 테스트케이스 검증)를 통해, 치명적인 실수를 잡아낼 수 있었습니다.

    문제의 테스트케이스들에서는 5*5배열만 제공했지만,
    택시거리(=맨해튼거리)가 제대로 반영됐는지를 확인하기 위해,
    7*7배열로 print()를 찍어보며 확인해 봤습니다.

    for i in range(catcher_y - 3, catcher_y + 3):
        for j in range(catcher_x - 3, catcher_x + 3):
    그 결과, 위와 같이 +3으로 표시되어
    end index가 +3이 아닌 +2까지만 for문에서 다뤄졌음을 확인할 수 있었습니다.

    테스트케이스에서 발견할 수 없는 실수였기에,
    커스텀 테케를 만들고 해당 모듈만을 print로 확인하는 검증루틴 4단계의 효용을 체감할 수 있었습니다.


    (1) 주어진 테스트케이스로 검증
        - k턴마다 도망자와 술래의 상태를 print로 확인
        - 술래가 나선형루트의 양쪽 끝부분에서 잘 움직이고 방향도 잘 트는지 확인
    (2) 메모 vs. 코드
    (3) (머릿속 환기 후) 문제 재정독
        - 6분(15:16 - 15:22) 동안 메모 재작성하며, 문제 정독&메모
        - 문제 새롭게 이해한 부분은 없었지만, 메모를 더 체계적으로 할 수 있었음
    (4) 커스텀 테스트케이스 검증
        - 7*7배열과 3*3배열에서도, 술래의 방향 설정이 잘 돼있는지 확인
        - 도망자 정상적으로 삭제되는지 확인
        - 위에 적힌 range() 치명적 실수 발견
    (5) 철저한 코드 검증
        - 시간상, 코드 재작성 X
        - 코드 정독
    (6) 오답노트 활용
        - 오답노트 먼저 보고 작성된 코드를 보며, 같은 실수 되풀이 유무 체크
    (7) 다양한 구상에 따른, 다른 구현
        - 모호한 부분 없었기에, 다른 구상&구현 X
"""

direction_runner = ((0, 1), (1, 0), (0, -1), (-1, 0))
direction_catcher = ((1, 0), (0, 1), (-1, 0), (0, -1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# 좌표/방향의 도망자에 대해, 이동 결과를 반환하는 함수
def move_runner(ry, rx, rd):
    # 현재 방향으로, 한 칸 가보기
    rdy, rdx = direction_runner[rd]
    nry, nrx = ry + rdy, rx + rdx

    # 영역 안
    if not oob(nry, nrx):
        if nry == catcher_y and nrx == catcher_x:  # 술래 좌표와 겹치면
            return ry, rx, rd
        else:                                      # 술래 좌표와 안 겹치면
            return nry, nrx, rd
    # 영역 밖
    else:
        # 반대방향으로 바꾸고, 한 칸 가보기
        rd = (rd + 2) % 4
        rdy, rdx = direction_runner[rd]
        nry, nrx = ry + rdy, rx + rdx
        if nry == catcher_y and nrx == catcher_x:  # 술래 좌표와 겹치면
            return ry, rx, rd
        else:                                      # 술래 좌표와 안 겹치면
            return nry, nrx, rd


# 이동 가능한 도망자들을 동시에 이동시키는 함수
def move_runners():
    moved_results = []  # 이동된 도망자들의 결과를 담을 배열

    # 현재 술래의 좌표 (-3 ~ +3) 범위에 대해서
    for i in range(catcher_y - 3, catcher_y + 4):
        for j in range(catcher_x - 3, catcher_x + 4):
            # 영역 안이고 택시거리 3이하면, 이동 가능
            if not oob(i, j) and abs(catcher_y - i) + abs(catcher_x - j) <= 3:
                moving_runners = runners[i][j]
                runners[i][j] = []  # 해당 좌표의 도망자 리스트 초기화

                # 현재 좌표의 도망자들 이동 처리
                for rd in moving_runners:
                    moved_results.append(move_runner(i, j, rd))

    # 이동된 도망자들의 이동 반영
    for ry, rx, rd in moved_results:
        runners[ry][rx].append(rd)


# 술래를 이동시키고, 방향 틀어주고, 도망자 잡는 함수
def move_catcher():
    global catcher_y, catcher_x, catcher_route_idx, catcher_route_reverse, total_score

    # 술래 좌표 이동
    dy, dx = direction_catcher[catcher_directions[catcher_route_reverse][catcher_route_idx]]
    catcher_y, catcher_x = catcher_y + dy, catcher_x + dx

    # 술래 방향 설정
    if catcher_route_reverse:
        catcher_route_idx -= 1
        if catcher_route_idx == 0:
            catcher_route_reverse = False
    else:
        catcher_route_idx += 1
        if catcher_route_idx == n**2 - 1:
            catcher_route_reverse = True
    dy, dx = direction_catcher[catcher_directions[catcher_route_reverse][catcher_route_idx]]

    # 도망자 잡기 & 점수 추가
    candidates = ((catcher_y, catcher_x), (catcher_y + dy, catcher_x + dx), (catcher_y + dy * 2, catcher_x + dx * 2))
    caught_runners_cnt = 0
    for cand_y, cand_x in candidates:
        if oob(cand_y, cand_x) or trees[cand_y][cand_x]:
            continue
        caught_runners_cnt += len(runners[cand_y][cand_x])
        runners[cand_y][cand_x] = []
    total_score += caught_runners_cnt * turn


n, m, h, k = map(int, input().split())

# N*N배열의 각 좌표에, 도망자들의 방향 index들이 리스트로 관리됨.
runners = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(lambda abc: int(abc) - 1, input().split())  # 1 -> 0(우) / 2 -> 1(하)
    runners[a][b].append(c)

# 나무의 존재 유무 배열
trees = [[0] * n for _ in range(n)]
for _ in range(h):
    a, b = map(lambda ab: int(ab) - 1, input().split())
    trees[a][b] = 1

# 술래의 나선형 이동 루트별 방향을 구하는 코드
visited = [[0] * n for _ in range(n)]  # (0,0)부터 나선형 회전을 위한 방문배열
visited[0][0] = 1
cy, cx, cd = 0, 0, 0  # (0,0)부터 아래쪽을 보고 시작

catcher_directions = [[], [0, ]]  # 0번 index: 중앙에서 바깥쪽으로의 이동별 방향 / 1번 index: 바깥쪽에서 중앙으로의 이동별 방향
while not (cy == n // 2 and cx == n // 2):
    cdy, cdx = direction_catcher[cd]  # (이전의 반복문에서 유효한 방향 설정돼 있음)
    cy, cx = cy + cdy, cx + cdx
    visited[cy][cx] = 1
    catcher_directions[0].append((cd + 2) % 4)  # 기존 이동방향의 반대 방향을, 중앙->바깥 이동별 방향리스트에 append

    ncy, ncx = cy + cdy, cx + cdx
    if oob(ncy, ncx) or visited[ncy][ncx]:
        cd = (cd + 1) % 4

    catcher_directions[1].append(cd)  # 다음의 유효한 방향을, 바깥->중앙 이동별 방향리스트에 append

# 이동루트 바깥부터 돌았으므로, 이동루트별 방향도 reverse
catcher_directions[0].reverse()
catcher_directions[1].reverse()
# 이동별 방향 미세조정
catcher_directions[0].append(0)
catcher_directions[1][0] = 2

# 초기의 술래 좌표/이동루트idx/이동루트 역이동 유무
# 이동루트idx 설정; ( 0은 중앙 / -1(== n**2-1)은 0,0 )
# 이동루트 역이동 유무: ( False는 중앙->바깥쪽 / True는 바깥쪽->중앙 )
catcher_y, catcher_x, catcher_route_idx, catcher_route_reverse = n // 2, n // 2, 0, False

# k턴 동안, 도망자이동&술래이동 반복
total_score = 0
for turn in range(1, k + 1):
    move_runners()
    move_catcher()
print(total_score)
