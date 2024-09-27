# 20240925
# 1:45:00
# 1 / 2

"""
풀이 시간: 1시간 45분 (09:03 - 10:48)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (09:03 - 09:14)
    문제에서 체스판 바깥 영역은 벽으로 간주한다고 했을 때,
    이 문제는 테두리를 2로 다 채워놓고 하면, 구현 과정에서 oob 분기처리가 많이 줄어들 문제로 예상했습니다.

    그리고 최근 문제들에서 정보의 중복 저장을 선호하지는 않아서,
    정보를 통합적으로 하나에서 관리하는 풀이 방식을 선호한 경향이 있었습니다.
    그러나, 이 문제는 기사위치정보 L*L배열을 만들어주는 것이 더 간단하게 구현될 것으로 생각했습니다.

    위와 같이, 평소에 선호하지 않았던 방식을 채택했기에, (채택 근거: 구현이 더 간단하고, 검증이 더 수월할 것으로 예상)
    구현 과정에서 더 꼼꼼히 해야 하고, 그에 따라 평소보다 구현 시간이 더 걸릴 것으로 예상했습니다.


2. 구현 (09:14 - 10:09)
    문제 지문 내의 그림 설명이 아니라면, 테케 밑에 있는 그림 설명을 보고 구현에 들어가는 편이 아닙니다.
    이유는, 문제 지문 내 설명 만으로, 문제조건/요구사항/엣지케이스를 더 온전히 이해하고 찾아내기 위해서입니다.
    그렇다 보니, 문제 지문에 대해 이해를 더 꼼꼼히 하지 않아서 아래의 오해를 했습니다.

    - 기사가 차지하는 칸은 1*1칸으로 오해 (-> 방패 범위 H*W는 대미지 계산에서만 반영되는 것으로 오해)
    그래서 13분(09:26-09:39) 동안, 해당 오해를 바탕으로 기사 이동 함수를 작성했고,
    해당 함수 구현 완료 후 체크포인트에서 오해를 바로잡고 다시 구현할 수 있었습니다.

    이러한 실수가 있었지만, 테케 설명을 보지 않는 루틴에 대해서는 수정할 계획이 없습니다.
    오히려, 그 전의 정독 단계에서 문제 지문을 더 온전히 이해하고 넘어가야 하고
    그 후의 검증 단계에서 테케 설명 분석을 더 꼼꼼히 해야할 것으로 회고했습니다.


3. 디버깅 (10:09 - 10:15)
    디버깅 단계에서 테케 설명의 한 단계씩 따라가며, 아래 오류들을 수정했습니다.
    - 피해 계산할 때, 함정이 아닌 벽을 기준으로 했던 것
    - 이동 전 위치 0으로 바꿔주는 작업 빠진 것
    - 왕명 받은 기사도 피해입었던 것


4. 검증 (10:15 - 10:48)
    O (1) 주어진 테스트케이스로 검증
        - 위의 검증 단계에서 마지막 실수였던 "왕명 받은 기사도 피해입었던 것"을 수정한 과정에서, 다시 실수가 있었음을 확인했습니다.
          테케의 흐름과 하나씩 비교하는 과정에서, 왕명 받은 기사가 움직이지 않은 것을 눈으로 확인하고, 이를 수정했습니다.
    O (2) 메모 vs. 코드
        - 메모와 비교검증하는 과정에서, 아래와 같은 상황이 생각났기에, move_knights 함수에 방문배열을 추가했습니다.
            예시) 124  : 1이 오른쪽으로 가는 경우, 2/3을 거져 4로 도달하는데 4가 중복 방문될 수도 있음.
                 134
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
        - 왕명받은 기사 피해 안 입고 움직이는지
        - 기사 사라짐 처리 온전하게 하는지
        - 최종답안 계산할 때, 사라진 기사 잘 건너뛰는지
        - 최소 범위 테케
        - 평소에 잘 활용하지 않았던 코드들 검증
            - set의 extend() / 컴프리헨션에서의 이중 for문
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
        - 이동 확정된 기사들을 이동시키는 과정에서, H*W 만큼 0으로 바꿨다가 다시 새로운 위치에 H*W 만큼 기사번호를 저장한 코드가 개선 가능했습니다.
          (그러나, 시간복잡도 체크에서 이상 없었고, 더 안전/검증쉬운 코드라고 생각했기에, 그대로 뒀습니다.)


5. 코드트리 미흡한 채점
    이동 순서 정확하게 검증되지 않아서, 이동 과정에서 기사를 지우는 이슈 있었음.
    코드트리에서 해당 케이스에 대한 채점테게가 없었어서 정답 처리 됐었음.
"""

from collections import deque

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 상우하좌


def get_edge_plus_1(top, left, height, width, d_idx):
    if d_idx == 0:
        return knights_arr[top - 1][left:left + width], area[top - 1][left:left + width]
    elif d_idx == 1:
        return [knights_arr[r][left + width] for r in range(top, top + height)], [area[r][left + width] for r in range(top, top + height)]
    elif d_idx == 2:
        return knights_arr[top + height][left:left + width], area[top + height][left:left + width]
    elif d_idx == 3:
        return [knights_arr[r][left - 1] for r in range(top, top + height)], [area[r][left - 1] for r in range(top, top + height)]


# 명령대로 움직일 수 있는지 체크하고, 명령대로 움직일 수 있다면 움직이는 기사들을 반환하는 함수
def move_knights(start_knight, d_idx):
    moving_knights = []  # 명령대로 움직일 수 있다면, 반환될 움직이는 기사들

    visited = []  # 방문체크 배열

    queue = deque()
    queue.append(start_knight)  # 왕명 받은 기사부터 움직여보기

    while queue:
        now_knight = queue.popleft()

        if now_knight in visited:  # 이미 방문 -> continue
            continue
        visited.append(now_knight)         # 방문 처리
        moving_knights.append(now_knight)  # 움직이는 기사 배열에 추가

        # 움직였을 때 새로 이동하는 곳의, knights_arr영역과  area영역
        next_knights_line, next_area_line = get_edge_plus_1(*knights_info[now_knight][:4], d_idx)
        if 2 in next_area_line:  # 새로 이동할 곳에 벽(2)이 있다면, 명령대로 이동 못함(return None)
            return None
        queue.extend(set(next_knights_line) - {0})  # 이동 가능하다면, 밀려서 이동하는 기사들(0 제외) queue에 추가

    return moving_knights


# 움직이는 게 확정된 기사들의 피해량을 계산하고, 정보를 갱신하는 함수
def cal_damage_and_renew_info(moving_knights, d_idx):
    # 기사들이 움직이는 방향
    dy, dx = direction[d_idx]

    for now_knight in moving_knights:
        knight_y, knight_x, knight_h, knight_w, knight_life = knights_info[now_knight]
        # 다음으로 움직이게 될 좌상단 좌표
        nky, nkx = knight_y + dy, knight_x + dx

        # 현재 기사가 왕명받은 기사가 아니라면, 피해량 반영
        if now_knight != command_knight:
            knight_life -= sum([area[r][c] == 1 for c in range(nkx, nkx + knight_w) for r in range(nky, nky + knight_h)])

        # 기존 위치 0으로
        for r in range(knight_y, knight_y + knight_h):
            for c in range(knight_x, knight_x + knight_w):
                if knights_arr[r][c] == now_knight:
                    knights_arr[r][c] = 0

        # 체력이 0이하가 되면 -> 체스판에서 사라짐 처리 (체력은 0으로)
        if knight_life <= 0:
            knights_info[now_knight] = -1, -1, -1, -1, 0
        # 체력 남아있다면 -> 다음 이동 위치 표시 & 정보(좌상단 좌표 & 체력) 갱신
        else:
            for r in range(nky, nky + knight_h):
                for c in range(nkx, nkx + knight_w):
                    knights_arr[r][c] = now_knight
            knights_info[now_knight] = nky, nkx, knight_h, knight_w, knight_life


l, n, q = map(int, input().split())
# 체스판 정보 (L+2)*(L+2) 배열 (테두리 벽(2)로 감싸줌)
area = [[2] * (l + 2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(l)] + [[2] * (l + 2)]

first_knights_lives = [None]  # 기사들의 초기 체력 (최종정답 계산용)
knights_info = [None] + [tuple(map(int, input().split())) for _ in range(n)]  # 기사들 정보(좌상단 좌표, H, W, 현재 체력) 배열
knights_arr = [[0] * (l + 2) for _ in range(l + 2)]  # 기사들 위치가 표시될 (L+2)*(L+2) 배열
for i in range(1, n + 1):
    ky, kx, kh, kw, k_life = knights_info[i]
    for ki in range(kh):
        for kj in range(kw):
            knights_arr[ky + ki][kx + kj] = i
    first_knights_lives.append(k_life)

# 왕명 Q회 수행
for _ in range(q):
    command_knight, command_d = map(int, input().split())

    # 체스판에서 사라진 기사에게 명령하면 -> 아무 반응 X (continue)
    if not knights_info[command_knight][-1]:
        continue

    # 명령대로 움직일 수 있는지 체크 (명령대로 움직일 수 있다면, 움직이는 기사들 번호 가져옴)
    moved_result = move_knights(command_knight, command_d)

    # 명령대로 움직일 수 없다면, 기사 정보 갱신할 필요 X
    if not moved_result:
        continue
    # 명령대로 움직일 수 있다면, 움직이는 기사들의 정보 갱신 O
    cal_damage_and_renew_info(moved_result, command_d)

alive_knights_damaged_sum = 0
for i in range(1, n + 1):
    k_life = knights_info[i][-1]
    if not k_life:
        continue
    alive_knights_damaged_sum += first_knights_lives[i] - k_life
print(alive_knights_damaged_sum)
