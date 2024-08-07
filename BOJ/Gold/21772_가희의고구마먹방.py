# 20240807
# 56:57
# 1 / 4

# 갔던 곳을 다시 못 간다고 생각해서, 시간이 걸렸던 문제.


def oob(yy, xx):
    return (yy < 0) or (n <= yy) or (xx < 0) or (m <= xx)


def dfs(y, x, distance, sweet_potatoes):  # 현재 좌표, 시작부터 현재까지의 거리(시간), 현재까지 찾은 고구마 수
    global mx
    if sweet_potatoes > mx:  # 만약 지금까지의 고구마가 더 크다면 갱신 (머무르는 옵션도 있기 때문에, 매번 체크해줌.)
        mx = sweet_potatoes
    elif t - distance <= mx - sweet_potatoes:  # 조기 종료조건: 앞으로 갈수 있는 시간보다, 고구마수와 최대값의 차이가 더 크거나 같은 경우
        return

    if distance == t:  # 시작지점부터 이동한 시간 오버되면, 종료
        return

    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or area[ny][nx] == '#':
            continue
        if area[ny][nx] == 'S':
            area[ny][nx] = '.'  # 고구마는 다시 자랄 수 없기에 값 변경 해주기
            dfs(ny, nx, distance + 1, sweet_potatoes + 1)
            area[ny][nx] = 'S'
        else:
            dfs(ny, nx, distance + 1, sweet_potatoes)


n, m, t = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

start = (None, None)
for i in range(n):
    for j in range(m):
        if area[i][j] == 'G':
            start = (i, j)  # 가희 좌표 찾으면 저장
            break
    else:
        continue
    break

mx = 0
dfs(start[0], start[1], 0, 0)  # 가희의 시작점을 기준으로 DFS 호출

print(mx)
