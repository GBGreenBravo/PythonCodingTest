# 20240912
# 45:00
# 1 / 1

"""
풀이 시간: 45분 (10:01 ~ 10:46)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (10:01 - 10:11)
    어제 팀 논의 시간에, 손 설계를 하는 경우
    글씨를 예쁘게 써야 눈에 더 잘 들어오고, 메모를 더 자주 읽게 된다는 이야기가 나왔기에,
    글씨를 너무 날려 쓰지 않도록 주의했습니다.

    문제를 다 읽고
    출발지/목적지가 벽에 막힌 경우도 있을 수 있겠다고 생각했고, 그에 대한 명확한 설명이 지문에 없었기에
    해당 케이스를 물음표 표시로 종이메모에 남겨놨습니다.


2. 구현 (10:11 - 10:33)
    최근에 정립해온 방식으로,
    메인 코드를 먼저 구현하여,
    독립적인 수행(함수화 할 부분)을 배제한, 큰 흐름의 구현을 먼저 했습니다.

    그리고 체크포인트 루틴 대로,
    입력 코드 작성, 함수 코드 작성이 끝난 시점마다 print()를 통해 확인했습니다.
    그 결과, 가장 가까운 승객을 찾는 함수(find_closest_passenger)에서
    next_queue에 append()해줘야 할 것을, queue에 append()했던 실수를 탐지할 수 있었습니다.


3. 검증 (10:33 - 10:46)
    구현이 끝나고 테스트케이스를 돌려본 결과, 에러나 오답이 확인되지 않았습니다.
    그랬기에, 더 잘 구현한 것인지 꼼꼼히 체크해줘야 한다고 생각했습니다.

    루틴 대로 아래의 체크사항들을 점검해줬습니다.
    1) 문제를 다시 천천히 읽어보며, 메모에 모든 사항이 적혔는지/문제를 잘못 이해한 부분은 없는지 체크
    2) 메모의 요구사항이 코드에 모두 반영됐는지 체크
    3) 메모에 작성해둔, 모호한 부분/엣지 케이스 가 코드에 반영됐는지 체크
    4) 과거에 했던 실수들 되풀이하지 않았는지 체크 (BFS에서 방문체크 안 해서 메모리 초과, break로 종료하는 반복문 체크 등)
    5) 확인 가능한 테스트케이스의 각 단계를 출력하며, 생각대로 넘어가는지 체크

    그리고 위의 2)과정에서 초기에 구현된 코드에서,
    가장 가까운 승객을 찾는 함수(find_closest_passenger)가 BFS기에 시간복잡도 O(N**2)로 구상했었는데,
    다음 좌표가 출발지점 중 하나인지를 비교하는 코드가 오른쪽과 같이 구현됐기에,  =>  if (ny, nx) in start_points
    시간 복잡도 O(N**2 * N**2)가 될 수 있겠다고 생각했습니다.
    따라서 in 연산의 시간복잡도를 줄이기 위해, 출발지점들을 그대로 갖는 start_points_set을 두어,
    해당 함수의 시간복잡도를 O(N**2)로 줄일 수 있었습니다.
    따라서 앞으로는 검증 단계에서, 코드의 시간복잡도도 생각대로 구현됐는지 체크하는 루틴을 추가해야겠습니다.

    => 아직 시간복잡도 계산을 잘 못해서 그런지, 초기 코드와 실행시간은 큰 차이가 없었습니다.
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# 가장 가까운 승객을 찾고, 택시를 그리로 이동시키고, (해당 승객 idx, 최단 거리)를 반환하는 함수
def find_closest_passenger():
    global ty, tx

    # 택시의 현재 위치에, 승차 기다리는 손님 있는 경우
    if (ty, tx) in start_points_set:
        return start_points.index((ty, tx)), 0

    # BFS
    visited = [[0] * n for _ in range(n)]
    visited[ty][tx] = 1

    queue = deque()
    queue.append((ty, tx))

    distance = 0  # 해당 위치까지의 거리 (= 해당 위치까지 소모되는 연료)
    while queue:
        next_queue = deque()
        distance += 1
        possible_at_this_distance = []  # 현재의 거리로 갈 수 있는, 승차시킬 승객들의 좌표

        while queue:
            y, x = queue.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or visited[ny][nx] or area[ny][nx]:  # 영역 밖 / 이미 방문 / 벽
                    continue
                visited[ny][nx] = 1
                next_queue.append((ny, nx))
                if (ny, nx) in start_points_set:  # 승차시킬 승객의 좌표 중 하나라면
                    possible_at_this_distance.append((ny, nx))

        # 현재의 거리(최단 거리)에, 승차시킬 승객 있다면
        if possible_at_this_distance:
            possible_at_this_distance.sort()  # 행번호 오름차순/열번호 오름차순 정렬
            ty, tx = possible_at_this_distance[0]  # 택시를 해당 승객의 좌표로 이동
            return start_points.index((ty, tx)), distance  # (해당 승객 idx, 최단 거리) 반환

        # 승차시킬 승객 아직 못 찾았다면, BFS 반복
        queue = next_queue

    return None  # 승차 기다리는 손님 있는데, 벽으로 모든 길이 막혀있다면, return None


# 현재 승객의 도착지점(ey, ex)까지 최단거리로 택시를 이동시키는 함수
def drive_to_end_point(ey, ex):
    global ty, tx, fuel

    # BFS
    visited = [[0] * n for _ in range(n)]
    visited[ty][tx] = 1

    queue = deque()
    queue.append((ty, tx))

    distance = 0
    while queue:
        next_queue = deque()
        distance += 1
        while queue:
            y, x = queue.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or visited[ny][nx] or area[ny][nx]:  # 영역 밖 / 이미 방문 / 벽
                    continue
                visited[ny][nx] = 1
                next_queue.append((ny, nx))
                # 도착지점(ey, ex)에 도달했다면
                if ny == ey and nx == ex:
                    fuel -= distance  # 이동시 소모한 연료 반영
                    if fuel < 0:      # 도착시 연료가 음수라면, 이동 실패 (return False)
                        return False
                    fuel += distance * 2  # (이동시 소모한 연료 * 2) 만큼 연료 충전

                    ty, tx = ny, nx  # 택시 위치 이동
                    return True
        queue = next_queue

    return False  # 도착지점이 벽으로 막혀 도달 못하면 return False


# 한 명의 승객을 찾고, 그로 이동하고, 해당 승객을 이동시키는 함수 (이동 실패 발생하면 return False)
def drive():
    global fuel

    find_result = find_closest_passenger()  # 가장 가까운 승객을 가져옴
    if not find_result:  # 다음 승객 못 찾은 경우 (다음 승객의 출발지가 벽에 막혀 못가는 경우)
        return False
    p_idx, used_fuel = find_result  # (해당 승객 idx, 그리로 가는데 소모된 연료)

    fuel -= used_fuel  # 연료 소모
    if fuel <= 0:  # 가장 가까운 승객에게 가는 길에 연료 다 소모되면, 이동 실패 (return False)
        return False

    start_points_set.remove(start_points[p_idx])  # 출발지점 set에서 제거
    del start_points[p_idx]                       # 출발지점 list에서 제거
    end_y, end_x = end_points.pop(p_idx)          # 도착지점 pop()

    if not drive_to_end_point(end_y, end_x):  # 현재 승객의 도착지점까지 가보고, 이동 실패하면 return False
        return False

    return True  # 현재 승객 이동 성공하면 return True


n, m, fuel = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]  # 빈칸/벽 정보 배열
ty, tx = map(int, input().split())  # 택시 좌표
ty, tx = ty - 1, tx - 1             # 택시 좌표 조정
start_points = []
start_points_set = set()  # in 연산을 위한, start_points의 출발지점들을 똑같이 저장하는 set()
end_points = []
for _ in range(m):
    aa, bb, cc, dd = map(int, input().split())
    start_points.append((aa - 1, bb - 1))   # 출발지점 list에 저장
    start_points_set.add((aa - 1, bb - 1))  # 출발지점 set에 저장
    end_points.append((cc - 1, dd - 1))     # 도착지점 저장

for _ in range(m):   # m명의 승객
    if not drive():  # 이동 해보고, False(실패)를 반환하는 경우
        print(-1)
        break
else:                # 모든 승객을 성공적으로 이동시킨 경우
    print(fuel)
