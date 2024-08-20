# 20240820
# 15:00
# 1 / 1

# 시간복잡도 계산: 10000개의 좌표를 십자가 길이 1씩 늘려주며 최대 50까지 체크하는데, 대충 계산해도 25 * 10**6이므로, 1초 내라고 생각했다.

# 이 풀이들은, 십자가 크기를 키워가며 모든좌표를 돌았는데, 시간복잡도 면에서 다른 풀이(좌표를 돌며 십자가 구성이 가능한 최대치를 찾기)가 더 나음.


def check_possible(length):  # 십자가 길이가 주어지면 그 길이로 배치 가능한 좌표들 체크하고 저장
    for r in range(length, n - length):  # 십자가 중심만 생각하고 반복문 돌기
        for c in range(length, m - length):
            if area[r][c] == '*':  # 십자가 중심이 *일 때,
                if len(set(area[r][c - length : c + length + 1])) == 1 and len(set([area[i][c] for i in range(r - length, r + length + 1)])) == 1:  # 가로/세로에 길이만큼 모두 *일때
                    possibles.append((length, r, c))  # 가능한 길이/좌표 저장


def fill(length, sr, sc):  # 주어진 십자가 길이와 중심 좌표에 대해, 십자가 영역만큼 .으로 바꾸는 함수
    for nc in range(sc - length, sc + length + 1):  # 가로 .으로 변환
        area[sr][nc] = '.'
    for nr in range(sr - length, sr + length + 1):  # 세로 .으로 변환
        area[nr][sc] = '.'


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

possibles = []  # 십자가 배치 가능한 (좌표, 십자가 길이)를 저장할 배열
for i in range(1, ((max(n, m) - 1) // 2) + 1):  # 1부터 가능한 십자가 길이까지
    check_possible(i)  # 현재 길이의 십자가 놓을 수 있는 좌표 체크

for l, pr, pc in possibles:  # 가능한 좌표들에 대해서
    fill(l, pr, pc)  # *을 .으로 바꾸기

for i in range(n):
    for j in range(m):
        if area[i][j] == '*':  # 하나라도 * 남아있다면, 불가능한 입력값이므로 -1 출력
            print(-1)
            break
    else:
        continue
    break
else:  # break 없으면 모든 좌표가 .이라는 말이므로 가능 / 요구하는 출력값 출력
    print(len(possibles))
    for l, pr, pc in possibles:
        print(pr + 1, pc + 1, l)


# 구현에서, 가능한지 계산하고, 나중에 possibles를 한꺼번에 덮었는데, 그럴 필요 없이 복사본 두고, 가능한지 계산하면서 그때 복사본에 덮어도 됨.
"""
def fill(length, sr, sc):  # area가 아닌 copied_area에 반영
    for nc in range(sc - length, sc + length + 1):
        copied_area[sr][nc] = '.'
    for nr in range(sr - length, sr + length + 1):
        copied_area[nr][sc] = '.'


def check_possible(length):
    for r in range(length, n - length):
        for c in range(length, m - length):
            if area[r][c] == '*':
                if len(set(area[r][c - length : c + length + 1])) == 1 and len(set([area[i][c] for i in range(r - length, r + length + 1)])) == 1:
                    possibles.append((length, r, c))
                    fill(length, r, c)  # 가능한 영역에 대해 복사본에 .으로 변환


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]
copied_area = [row[:] for row in area]  # area에서는 계산 중에 *->. 바뀌면 안되므로, .으로의 변환을 해줄 복사본

possibles = []
for i in range(1, ((min(n, m) - 1) // 2) + 1):
    check_possible(i)

for i in range(n):
    for j in range(m):
        if copied_area[i][j] == '*':
            print(-1)
            break
    else:
        continue
    break
else:
    print(len(possibles))
    for l, pr, pc in possibles:
        print(pr + 1, pc + 1, l)
"""