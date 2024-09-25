# 20240925
# 1 / 1
# 12:04

# 중력 왼쪽으로 작용 연습

n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

# (중력 왼쪽으로 작용하기에) 시계방향 회전
area = [list(row)[::-1] for row in zip(*area)]

# 중력 작용 끝까지 해주기 위해, 행 끝에 장애물(#) 추가
for row in area:
    row.append('#')

# before, after : 모두 장애물(#)의 좌표로, 이 사이에 중력작용 반영하면 됨.
last_obstacle_idx = len(area[0]) - 1  # 행별 마지막 장애물의 index
for r in range(len(area)):
    before = -1  # 0부터 중력작용 시켜줘야 하므로, -1에 가상의 장애물(#) 있다고 가정

    # 현재 r행에 중력작용 반영
    while True:
        # before 다음의 장애물(#) 열index 찾기
        for col in range(before + 1, last_obstacle_idx + 1):
            if area[r][col] == '#':
                after = col
                break

        # 중력작용 반영할 영역 (before과 after 사이)
        origin = area[r][before + 1:after]
        if origin:
            empty_size = origin.count(".")  # 빈칸 개수
            origin = [o for o in origin if o != '.'] + ['.'] * empty_size  # 빈칸은 모두 뒤로
            for col in range(len(origin)):
                area[r][before + 1 + col] = origin[col]  # 중력작용 적용한 결과를 area에 반영
        # 벽 연속한 경우는 origin 없기에 반영 X
        else:
            pass
        # before 장애물을 after로 갱신
        before = after

        # after이 last_obstacle_idx가 되면 종료 (이 뒤에는 중력작용 반영할 곳 없기에)
        if after == last_obstacle_idx:
            break

# (중력 왼쪽으로 작용을 가정하고 처음에 시계방향 회전 해줬기에) 반시계방향 회전으로 복구
area = [list(row) for row in reversed(list(zip(*area)))]
for row in area[1:]:  # 0행은 중력작용 종료 위한 장애물(#) 추가됐던 행이므로 배제
    print(*row, sep="")
