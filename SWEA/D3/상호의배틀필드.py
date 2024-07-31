# 20240731

# .index()를 dictionary로 바꾸는 게 더 나음.

T = int(input())
for test_case in range(1, T + 1):
    h, w = map(int, input().split())
    mp = [list(str(input())) for _ in range(h)]
    commands_length = int(input())
    commands = list(str(input()))

    direction = ((0, 1), (0, -1), (1, 0), (-1, 0))  # 동서남북 순으로 저장
    looking_index = None  # 현재 탱크가 바라보고 있는 방향
    tank = (None, None)  # 현재 탱크 좌표

    for i in range(h):
        for j in range(w):
            if mp[i][j] in [">", "<", "v", "^"]:  # 탱크 찾고 정보 저장
                tank = (i, j)
                looking_index = [">", "<", "v", "^"].index(mp[i][j])

    for command in commands:
        y, x = tank
        if command in ["R", "L", "D", "U"]:  # 동서남북 커맨드라면
            dy, dx = direction[["R", "L", "D", "U"].index(command)]  # 방향 찾고
            ny, nx = y + dy, x + dx  # 다음 갈 좌표 구하고
            looking_index = ["R", "L", "D", "U"].index(command)  # 탱크 보는 방향 바꿔주고
            mp[y][x] = [">", "<", "v", "^"][looking_index]  # 그에 따라 탱크 방향도 변경
            if 0 <= ny < h and 0 <= nx < w and mp[ny][nx] == '.':  # 가고자 하는 곳이 평지라면
                tank = ny, nx
                mp[y][x] = "."
                mp[ny][nx] = [">", "<", "v", "^"][["R", "L", "D", "U"].index(command)]

        elif command == "S":  # 슈팅 커맨드라면
            dy, dx = direction[looking_index]  # 쏠 방향 정하고
            distance = 0
            while True:  # 반복문 돌며 포탄 트래킹
                distance += 1
                ny, nx = y + dy * distance, x + dx * distance
                if not(0 <= ny < h) or not(0 <= nx < w) or mp[ny][nx] == "#":  # 범위 밖이거나 강철벽이면 break
                    break
                elif mp[ny][nx] == "*":  # 벽돌벽이면 평지로 바꾸고 break
                    mp[ny][nx] = "."
                    break

    print(f"#{test_case}", end=" ")
    for i in range(h):
        print(*mp[i], sep="")
