# 20240819
# 10:00
# 1 / 1

# 이번 풀이에서는 큰 숫자부터 채웠지만, 규칙성 발견해서 작은 숫자(1)부터 채우는 것도 가능.

# 13567_로봇 문제와 마찬가지로, 방향 설정이 필요했음.
direction = ((1, 0), (0, 1), (-1, 0), (0, -1))  # (+1)%4 할수록 반시계방향 90도 회전할 수 있도록 구성


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or n <= xx


n = int(input())
target = int(input())
area = [[0] * n for _ in range(n)]

now_num = n ** 2
y, x = 0, 0
direction_idx = 0  # direction의 현재 index
area[y][x] = now_num  # 첫 칸에 숫자 삽입
target_index = (1, 1)  # 타겟 넘버의 좌표
now_num -= 1  # 다음으로 삽입할 숫자
while now_num > 0:  # 1 삽입한 후, 0 넣을 자리 없으므로 종료
    dy, dx = direction[direction_idx]  # 현재 방향
    ny, nx = y + dy, x + dx  # 현재 방향에 따른 다음 좌표
    if oob(ny, nx) or area[ny][nx]:  # 다음 좌표가 영역 밖이거나 이미 채워져 있으면
        direction_idx += 1  # 방향 바꾸고, continue
        direction_idx %= 4
        continue
    area[ny][nx] = now_num  # 유효한 다음좌표에 숫자 삽입
    if now_num == target:  # 현재 삽입하는 숫자가 타겟 숫자라면
        target_index = (ny + 1, nx + 1)
    now_num -= 1  # 다음 수 지정
    y, x = ny, nx  # 현재 좌표 갱신

for row in area:
    print(*row)
print(*target_index)
