# 20240823
# 28:00
# 1 / 1

"""
풀이 시간: 28분 (14:30 ~ 14:58)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:30 - 14:39)
    핵심은 구름이 경계를 이동하는 경우를 구분시켜주는 것이라고 생각했습니다.
    경계를 이동하는 s가 n의 범위를 초과할 수 있기 때문에,
    while문을 통해 영역 내로 조정될 때까지 값을 변경시켜야겠다고 계획했습니다.

    그리고 구름이 이동할 때는 8방향으로 갈 수 있지만,
    추가적인 비가 내릴 때는 대각선 4방향으로만 갈 수 있기에,
    해당 direction을 8방향으로 기본으로 하고,
    구현 과정에서 index로 접근하는 것보다, 대각선4방향을 따로 저장하는 것이 편하다고 하면 그때 추가하기로 했습니다.


2. 구현 (14:39 - 14:54)
    초기 상태에 대한 설명과 종료 조건을 제외하면,
    반복되는 동작은 문제의 1. 2.와 같이 체계적으로 표시되었기에,
    해당 사항에 대한 초기 메모를 바탕으로, 요구하는 조건들을 살펴가며 구현했습니다.


3. 검증 (14:54 - 14:58)
    8방향에 대한 index 실수

    구현을 마치고 처음으로 파일을 실행시켰을 때, 무한루프가 돌았습니다.
    이유는 8방향에 대한 튜플(direction_8)이 한 index씩 앞당겨져 있었기 때문입니다.

    위 오류를 범하고 디버깅하기 위해, 테스트케이스1번의 각 과정과 비교하기 위해,
    명령 수행 후의, 바구니 물 상태(area)를 print했습니다.
    이를 통해, 첫 수행부터 방향이 틀린 것을 발견하고, 바로 수정해 줬습니다.

    0번 인덱스가 남동쪽이 되어야 한다는 것을 문제를 읽으면서부터 인지했으나,
    초기 메모 과정에서 남동쪽을 8이라는 입력 그대로 적었고,
    0으로 바꿔줘야 한다는 표시를 해주지 않아 실수를 범한 것 같습니다.

    이러한 입력과 다른 코드 내의 인덱스 변경의 경우에도,
    메모 과정에 더 반영해야 함을 느꼈습니다.
"""

# 구름이 이동하는 8방향 (남동쪽부터 시계방향)
direction_8 = ((1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0))
# 추가로 비 내리는 대각선 4방향
direction_4 = ((-1, -1), (-1, 1), (1, 1), (1, -1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# 좌표가 주어질 때, 해당 좌표를 영역 내로 변경시키는 함수
def reshape(y, x):
    # 인자로 들어온 좌표가, 영역 내에 있으면 그대로 return
    if not oob(y, x):
        return y, x

    # 행 좌표가 영역을 벗어났다면, 들어올 때까지 조정
    while not(0 <= y < n):
        if y < 0:
            y += n
        elif n <= y:
            y -= n

    # 열 좌표가 영역을 벗어났다면, 들어올 때까지 조정
    while not(0 <= x < n):
        if x < 0:
            x += n
        elif n <= x:
            x -= n

    # 영역 내로 조정된 좌표를 반환
    return y, x


# 문제에서 명시된 1~5의 반복작업을 수행하는 함수
def raining(cloud_d, cloud_s):
    dy, dx = direction_8[cloud_d]

    # 초기 구름에서 방향/거리 만큼 이동된 유효한 좌표들을 담을 배열
    # ( = 이번 수행에서 사라질 구름 좌표들)
    moved_clouds = set()

    # 초기 구름 좌표들에 대해, 유효한 좌표들로 이동
    for cy, cx in now_clouds:
        ny, nx = cy + dy * cloud_s, cx + dx * cloud_s
        ny, nx = reshape(ny, nx)  # 영역 밖으로 변경될 수도 있으므로, 체크하고 조정
        moved_clouds.add((ny, nx))

    # 현재 구름들이 위치한 바구니 물양 += 1
    for my, mx in moved_clouds:
        area[my][mx] += 1

    # 추가로 내릴 비 적용
    for my, mx in moved_clouds:
        more_rain = 0
        for dy, dx in direction_4:  # 대각선 4방향에 대해
            ny, nx = my + dy, mx + dx
            if oob(ny, nx) or not area[ny][nx]:  # 영역 밖의 대각선이거나 or 바구니에 물이 없다면, continue
                continue
            more_rain += 1
        area[my][mx] += more_rain

    now_clouds.clear()  # 새로운 구름 탐색을 위해, clear

    for i in range(n):
        for j in range(n):
            # 물 양이 2 이상이고 and 이 수행에서 사라진 구름 좌표가 아니라면, 구름 생성
            if area[i][j] >= 2 and (i, j) not in moved_clouds:
                now_clouds.append((i, j))
                area[i][j] -= 2


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]  # 바구니의 물 양이 저장되는 배열

cloud_moves = [tuple(map(int, input().split())) for _ in range(m)]  # 구름이 이동하는 방향과 거리가 저장된 배열

# 문제에 명시된, 초기 구름의 위치
now_clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

# 구름 이동 명령에 따른, 함수 호출
for d, s in cloud_moves:
    if d == 8:  # 남동쪽의 방향 index를 0으로 설정했기에, 변경
        d = 0
    raining(d, s)

print(sum(map(sum, area)))  # 바구니 물양의 총합 출력
