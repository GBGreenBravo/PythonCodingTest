# 20240822
# 20:00
# 1 / 1

"""
풀이 시간: 20분 (14:51 ~ 15:11)
풀이 시도: 1 / 1

1. 문제 정독 & 풀이 구상 (14:51 - 14:58)

2. 구현 (14:58 - 15:09)

3. 검증 (15:09 - 15:11)

"""

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북동남서
next_direction = [3, 0, 1, 2]  # 반시계로 회전; 북동남서 -> 서북동남

n, m = map(int, input().split())
sy, sx, direction_idx = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

cleaned = [[0] * m for _ in range(n)]  # 좌표별 청소여부 체크하는 배열
y, x = sy, sx  # 아래의 반복문에서 사용되는 좌표 y, x

while True:
    # 현재의 청소되지 않은 빈칸, 청소 처리
    if not cleaned[y][x]:
        cleaned[y][x] = 1
        continue

    for i in range(4):  # 4방향에 대해 '빈칸'and'청소X'를 체크
        next_direction_idx = next_direction[(direction_idx + i) % 4]
        dy, dx = direction[next_direction_idx]  # 현재 반복문에서의 방향
        ny, nx = y + dy, x + dx
        if area[ny][nx] or cleaned[ny][nx]:  # 벽이거나 or 청소된빈칸
            continue
        direction_idx = next_direction[direction_idx]  # 왼쪽으로 90도 회전
        ddy, ddx = direction[direction_idx]
        nny, nnx = y + ddy, x + ddx  # 회전한 방향으로 전진했을 때의 좌표
        if not area[nny][nnx] and not cleaned[nny][nnx]:  # 앞으로 이동할 수 있다면 이동
            y, x = nny, nnx
        break
    else:  # 4방향에 '빈칸'and'청소X'가 하나도 없으면
        dy, dx = direction[direction_idx]
        ny, nx = y - dy, x - dx
        if not area[ny][nx]:  # 후진 가능하면
            y, x = ny, nx
        else:  # 후진 불가능하면
            break

print(sum(map(sum, cleaned)))
