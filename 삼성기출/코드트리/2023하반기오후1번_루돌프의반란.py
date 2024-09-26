# 20240925
# 1:57:00
# 1 / 2

"""
풀이 시간: 1시간 57분 (14:01 - 15:58)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (14:01 - 14:20)
    이제까지의 기출 문제들 중, 문제 지문이 가장 길었던 문제로 생각합니다.
    그래서 지문을 읽고 꼼꼼히 메모하는 과정에서,
    원래는 1장 정도 쓰는 걸, 이번 문제에서 1장 반을 넘게 메모했습니다.

    조금은 조급한 마음에 문제를 읽다 보니,
    현재 지문을 앞에 읽었던 내용과 온전히 연결해서 이해하지 않았고
    & 현재 읽고 있는 지문도 확실히 암기하지 않고 적어두고만 넘어가기도 했던 것 같습니다.

    디버깅 과정에서, 이 미흡한 이해&암기로 인한 실수들이 많이 발견됐기에
    & 20분도 오래 읽은 것은 아니기에
    => 문제 지문이 길어도 조급해하지 말고, 더 천천히 & 더 꼼꼼히 읽어야 할 것입니다.

    그리고 구상 단계에서, 생각하는 구상의 시간복잡도를 명확히 계산하지 않아,
    충분한 검증을 하지 못하고, 다른 시도를 하다가 급하게 제출했고 틀렸기에,
    구상 단계에서, 확실히 시간복잡도를 계산하고 넘어가야 합니다.


2. 구현 (14:20 - 15:02)


3. 디버깅 (15:02 - 15:26)
    이 문제를 구현하는 과정에서 자잘한 실수 + 큰 실수가 많았습니다.
    아래에는 큰 실수들만 적어놨습니다.
    - 루돌프 이동에서 가까운 산타를 찾아야 할 때, 기준 하나를 빼먹은 것
    - 루돌프가 밀려나는 거리 c를 변수로 받아놓고, 다른 입력을 받을 때 임시 변수명으로 또 c를 선언한 실수.
        - Ctrl+F7으로 모든 변수들이 선언/사용된 곳을 찾는 과정에서 발견할 수 있었습니다.


4. 검증 (15:26 - 15:33)
    검증 루틴 2단계에서, 시간복잡도를 계산해주는 과정에서 기존 풀이가 자칫하면 시간초과가 날 수도 있겠다고 판단했습니다.
    기존 풀이가 시간초과나는 경우는 최악의 케이스지만, 혹시 몰라서 시간적으로 명확한 풀이로 풀어야겠다고 생각했고,
    그 구현&디버깅을 20분 간 했습니다.
    기존 코드에 빨리 추가하려 하니, 평소 쓰는 스타일 대로 구현하지 못하고 꽤나 복잡하게 구현했습니다.
    그래서인지 디버깅 과정에서 실수들을 잡아낼 수 없었고,
    남은 시간이 얼마 남지 않아, 기존 코드를 불러와서 제출했습니다.

    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
        - 기존 풀이가 시간복잡도 이슈가 있을 것으로 예상하여 (7)단계로 바로 감
    X (3) (머릿속 환기 후) 문제 재정독
    X (4) 커스텀 테스트케이스 검증
    X (5) 철저한 코드 검증
    X (6) 오답노트 활용
    O (7) 다양한 구상에 따른, 다른 구현
        - (15:33 - 15:52)


5. 틀렸습니다 (15:52 - 15:58)
    충분한 검증 없이 제출한 코드였기에, 제출할 때도 확신 없이 조급한 마음에 제출했습니다.
    틀렸습니다가 떴고, 테스트케이스 8번을 확인할 수 있었습니다.
    Local History를 확인해서, 이전의 print디버깅 코드를 가져왔고 슬쩍 봤지만,
    일일이 따라가는 것이 어렵고 시간도 많이 소모될 것으로 생각했습니다.

    그래서 이런 경우에 어떻게 할지 미리 생각해뒀던 아래의 로직에 따라 수행했습니다.
    1) 문제 이해에 모호한 부분이 있었다면 => (이해 온전히 될 때까지) 해당 문제지문 다시 읽어보기
        1-1) 기존 코드가 오해를 바탕으로 작성됐다면 => 코드 수정
        1-2) 기존 코드가 틀린 부분이 없다고 생각되면 => 2)로
    2) 문제 이해에 모호한 부분이 없었다면 => 작성된 전체 코드를 한번 정독 & 꼼꼼히 검증
        2-1) 코드 오류 발견 => 코드 수정
        2-2) 코드 오류 미발견 => 문재 재정독 후 (부분적/전체) 코드 리셋

    위의 2-1)에서 실수를 발견할 수 있었습니다.
    산타가 루돌프와 충돌하는 경우, santa_stunned[s_idx] = 2 로 했어야 할 것을,
    =가 아닌 +=로 작성했음(14:52)을 발견하고, 수정했습니다.

    기존 코드가 시간복잡도에서 확신이 없었기에, 다른 구상대로 구현을 했어야해서
    검증 루틴을 다 소화하지 못해 발견 안된 실수였습니다.

    다음에 이러한 일이 생기지 않게 아래의 회고를 할 수 있었습니다.
    1) 구상 단계에서 구상의 시간복잡도를 더 명확히 계산해야 하고,
    2) 그럼에도 다른 구상을 해야할 상황이 생긴다면,
       (기존 코드에 대한 확신 정도를 고려해서)
       확신이 큰 편    =>  기존 코드 검증루틴 모두 소화 후 다른 구상으로 구현 시작
       확신이 작은 편  =>  다른 구상 바로 구현 시작
"""

direction_8 = ((-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))  # 상우하좌~


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def cal_distance(y1, x1, y2, x2):
    return (y1 - y2) ** 2 + (x1 - x2) ** 2


# (밀려난 산타가 다른 산타와 겹치는 경우에) 상호작용하는 함수
# 연쇄 가능하기에 재귀 호출 함수로 구현
# moving_s_idx: 밀려나고 있는 산타
# origin_s_idx: 그 자리에 원래 있던 산타
def communicate(moving_s_idx, origin_s_idx, d_idx):
    origin_y, origin_x = santas[origin_s_idx]

    # 밀리는 자리에, 밀리고 있던 산타 배정
    santas[moving_s_idx] = (origin_y, origin_x)

    # 원래 있던 산타가 밀리게 되는 위치
    dy, dx = direction_8[d_idx]
    ny, nx = origin_y + dy, origin_x + dx

    # 밀리게 되는 위치가 게임판 밖 -> 탈락 처리
    if oob(ny, nx):
        santas[origin_s_idx] = None
        return

    # 밀리게 되는 위치가 다른 산타와 겹친다면 -> 상호작용 (communicate() 재귀 호출)
    for osi, other in enumerate(santas):
        if not other:
            continue
        if other[0] == ny and other[1] == nx:
            return communicate(origin_s_idx, osi, d_idx)

    # 밀리게 되는 위치에 산타 없다면 -> 그 자리에 산타 배정
    santas[origin_s_idx] = (ny, nx)


# 루돌프와 산타를 충돌시키는 함수
# ('산타이동/루돌프이동'으로 인한 충돌 동시에 처리됨)
def collide(s_idx, distance, d_idx):
    # 충돌로 밀리는 거리만큼 점수 추가
    santa_score[s_idx] += distance

    # 충돌한 산타 기절 처리
    santa_stunned[s_idx] = 2

    # 충돌로 밀려나는 산타 위치 (ny, nx)
    sy, sx = santas[s_idx]
    dy, dx = direction_8[d_idx]
    ny, nx = sy + dy * distance, sx + dx * distance

    # 밀려난 위치가 게임판 밖 -> 탈락 처리
    if oob(ny, nx):
        santas[s_idx] = None
        return

    # 밀려난 위치가 다른 산타와 겹치면 -> 상호작용(communicate() 호출)
    for osi, other in enumerate(santas):
        if not other:
            continue
        if other[0] == ny and other[1] == nx:
            return communicate(s_idx, osi, d_idx)

    # 밀려난 위치가 다른 산타와 겹치지 않으면 -> 그 자리에 산타 놓기
    santas[s_idx] = (ny, nx)


def rudolph_move():
    global rudolph_y, rudolph_x

    # 가장 가까운 산타 찾기
    target_santa = (100**2 + 100**2, -1, -1, -1, -1)
    for santa in santas:
        if not santa:
            continue
        target_santa = min(target_santa, (cal_distance(rudolph_y, rudolph_x, *santa), -santa[0], -santa[1], *santa))

    # 가까운 산타에 가장 가까워지는 위치/이동방향 찾기
    next_rudolph = (100**2 + 100**2, -1, -1)
    for d_idx, (dy, dx) in enumerate(direction_8):
        ny, nx = rudolph_y + dy, rudolph_x + dx
        next_rudolph = min(next_rudolph, (cal_distance(ny, nx, *target_santa[3:]), ny, nx, d_idx))

    # 루돌프의 다음 위치/이동방향
    rudolph_y, rudolph_x, rudolph_d = next_rudolph[1:]

    # 산타 위치와 겹치면 -> 충돌(collide() 호출)
    for s_idx, santa in enumerate(santas):
        if not santa:
            continue
        if santa[0] == rudolph_y and santa[1] == rudolph_x:
            return collide(s_idx, c, rudolph_d)


# (탈락X and 기절X) 산타를 이동시키는 함수
def santa_move(s_idx):
    sy, sx = santas[s_idx]
    origin_distance = cal_distance(sy, sx, rudolph_y, rudolph_x)  # 기존 자리에서의 루돌프와의 거리

    # 이동 가능한 방향/위치 계산
    possibles = []
    for d_idx, (dy, dx) in enumerate(direction_8[:4]):
        ny, nx = sy + dy, sx + dx
        if oob(ny, nx):
            continue
        for osi, other in enumerate(santas):
            if not other:
                continue
            if ny == other[0] and nx == other[1]:
                break
        else:
            new_distance = cal_distance(ny, nx, rudolph_y, rudolph_x)
            if new_distance < origin_distance:
                possibles.append((new_distance, d_idx, ny, nx))

    # 이동할 수 없다면, 그 자리 그대로 두기
    if not possibles:
        return

    # 정렬 -> 가까워지는 순 / 상우하좌 순
    possibles.sort()
    santa_d, santa_y, santa_x = possibles[0][1:]
    # 해당 자리로 산타 옮기기
    santas[s_idx] = (santa_y, santa_x)

    # 루돌프와 겹친다면 -> 충돌 (collide() 호출)
    if santa_y == rudolph_y and santa_x == rudolph_x:
        return collide(s_idx, d, (santa_d + 2) % 4)  # 산타 이동으로 루돌프와 충돌하므로, 산타이동 반대방향


n, m, p, c, d = map(int, input().split())
# 루돌프 위치
rudolph_y, rudolph_x = map(lambda rud: int(rud) - 1, input().split())

# 산타 위치
santas = [None] * p
for _ in range(p):
    aa, bb, cc = map(int, input().split())
    santas[aa - 1] = (bb - 1, cc - 1)

santa_score = [0] * p    # 산타 점수
santa_stunned = [0] * p  # 산타 기절 상태

for _ in range(m):
    # 루돌프 이동
    rudolph_move()

    # (탈락X and 기절X)인 경우 -> 산타 이동
    for si in range(p):
        if santas[si] and not santa_stunned[si]:
            santa_move(si)

    # 산타 다 탈락했다면 -> 즉시 종료(break)
    if not sum([bool(s) for s in santas]):
        break

    # 턴 종료 후처리
    for si in range(p):
        # 탈락한 산타는 continue
        if not santas[si]:
            continue

        # 점수 += 1
        santa_score[si] += 1

        # 기절한 산타 기절시간-=1
        if santa_stunned[si]:
            santa_stunned[si] -= 1

print(*santa_score, sep=" ")
