# 20240902
# 27:00
# 1 / 1

from collections import deque

direction = ((0, 0), (-1, 0), (0, 1), (1, 0), (0, -1))


def oob(y, x):
    return y < 0 or 10 <= y or x < 0 or 10 <= x


# AP 좌표, 충전범위, 성능을 받아, 해당 범위 모두에 (성능, 좌표)를 추가하는 BFS 함수
def set_ap(sy, sx, c, p):
    visited = [[0] * 10 for _ in range(10)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx, 0))

    area[sy][sx].append((p, (sy, sx)))  # 영역에 (성능, 좌표)를 추가

    while queue:
        y, x, distance = queue.popleft()

        if distance == c:
            continue

        for dy, dx in direction[1:]:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx]:
                continue
            visited[ny][nx] = 1
            queue.append((ny, nx, distance + 1))
            area[ny][nx].append((p, (sy, sx)))  # 영역에 (성능, 좌표)를 추가


t = int(input())
for test_case in range(1, t + 1):
    area = [[[] for _ in range(10)] for _ in range(10)]  # 현재 좌표에 영향 미치는 AP가 들어갈 배열

    m, bc_cnt = map(int, input().split())
    a_moves = [0] + list(map(int, input().split()))  # 시작 위치에서도 충전하므로 [0] 앞에 추가
    b_moves = [0] + list(map(int, input().split()))  # 시작 위치에서도 충전하므로 [0] 앞에 추가

    for _ in range(bc_cnt):
        apx, apy, ap_coverage, ap_performance = map(int, input().split())
        set_ap(apy - 1, apx - 1, ap_coverage, ap_performance)  # AP의 영향 범위에, (성능, 좌표)를 저장
    for i in range(10):
        for j in range(10):
            area[i][j].sort(reverse=True)  # 좌표별 성능 내림차순으로 정렬

    answer = 0

    ay, ax = 0, 0  # a의 시작위치
    by, bx = 9, 9  # b의 시작위치
    for i in range(m + 1):
        # a, b 위치 갱신
        day, dax = direction[a_moves[i]]
        dby, dbx = direction[b_moves[i]]
        ay, ax = ay + day, ax + dax
        by, bx = by + dby, bx + dbx

        # 현재 a,b의 위치에 영향을 미치는 충전량
        a_charges = area[ay][ax]
        b_charges = area[by][bx]

        if not a_charges and not b_charges:  # 둘다 범위에 없다면
            pass
        elif not a_charges and b_charges:  # b만 범위에 있다면
            answer += b_charges[0][0]
        elif a_charges and not b_charges:  # a만 범위에 있다면
            answer += a_charges[0][0]
        else:  # 둘다 범위에 있다면
            if a_charges[0] != b_charges[0]:  # 두 최대 충전량 다르다면
                answer += a_charges[0][0] + b_charges[0][0]
            else:  # 두 최대 충전량 같다면
                a_candidate = a_charges[1][0] if len(a_charges) > 1 else 0  # 2개 이상이라면 차선책, 아니면 0
                b_candidate = b_charges[1][0] if len(b_charges) > 1 else 0  # 2개 이상이라면 차선책, 아니면 0
                candidate = max(a_candidate, b_candidate)  # 차선책 중 최대값
                answer += a_charges[0][0] + candidate  # '최대값 분할' or '최대값 + 차선책' 추가

    print(f"#{test_case} {answer}")  # a,b의 누적 충전량 출력
