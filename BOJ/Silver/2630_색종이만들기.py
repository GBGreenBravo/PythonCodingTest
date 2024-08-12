# 20240812
# 34:40
# 1 / 1


def check(left_top, right_down):  # 왼쪽위 좌표와 오른쪽 아래 좌표를 받아, 같은색인지 체크해보고 아니라면 4개로 나눠서 재귀로 return하는 함수
    sy, sx = left_top  # 왼쪽 위 좌표
    ey, ex = right_down  # 오른쪽 아래 좌표

    criteria = papers[sy][sx]  # 기준이 되는 색
    for i in range(sy, ey + 1):
        for j in range(sx, ex + 1):
            if papers[i][j] != criteria:  # 하나라도 색이 다르면 break
                break
        else:
            continue
        break
    else:  # 모든 좌표의 색이 같으면
        global paper_cnt
        paper_cnt[criteria] += 1  # 해당되는 색의 카운트 += 1 하고 return
        return

    length = (ey - sy + 1) // 2  # 하위 색종이의 길이
    for i in range(2):
        for j in range(2):
            ny, nx = sy + length * i, sx + length * j  # ny, nx는 다음 하위 색종이 4개 각각의 왼쪽 위 좌표가 됨.
            check((ny, nx), (ny + length - 1, nx + length - 1))  # 오른쪽 아래 좌표도 계산하여, 재귀함수


n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]

paper_cnt = [0, 0]  # 0: 하얀색 / 1: 파란색
check((0, 0), (n - 1, n - 1))

print(*paper_cnt, sep="\n")
