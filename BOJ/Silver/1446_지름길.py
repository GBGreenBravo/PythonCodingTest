# 20240814
# 18:17
# 1 / 1


def dfs(cnt, start):  # 현재 지름길 배열에 저장된 지름길 수, 현재 함수에서 탐색 시작할 지름길 index
    global mx_cut
    mx_cut = max(mx_cut, sum([i[2] for i in arr]))  # 지름길 단축 거리 최대값 갱신

    if start == len_valid:  # 유효한 지름길 배열 범위 밖이면 종료
        return

    for i in range(start, len_valid):
        now_valid_cut = valid_cuts[i]
        if arr and now_valid_cut[0] < arr[-1][1]:  # 현재 배열의 마지막에 선택한 지름길과 겹친다면, continue
            continue
        arr.append(now_valid_cut)
        dfs(cnt + 1, i + 1)
        arr.pop()


n, d = map(int, input().split())
short_cuts = [tuple(map(int, input().split())) for _ in range(n)]

valid_cuts = []  # 유효한 지름길만 저장할 배열
for s, e, distance in short_cuts:
    if e > d:  # 끝나는 지점이, 도착위치보다 큰 경우 -> 유효하지 않음.
        continue
    if e - s - distance <= 0:  # 단축되는 거리가 0이거나 음수일 경우 -> 단축이 안되므로 유효한 지름길 아님.
        continue
    valid_cuts.append((s, e, e - s - distance))  # [2]에 지름길 거리가 아닌, 해당 지름길이 단축시켜주는 거리를 저장
valid_cuts.sort()  # 유효한 지름길, 시작위치/끝위치 오름차순 정렬
len_valid = len(valid_cuts)

mx_cut = 0  # 가능한 지름길 조합 중, 가장 큰 단축 거리를 저장
arr = []  # 지름길 조합이 저장될 배열
dfs(0, 0)

print(d - mx_cut)  # 전체 거리에서, 지름길 최대 단축 거리를 빼서 출력
