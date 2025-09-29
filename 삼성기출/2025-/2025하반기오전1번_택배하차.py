# 20250929
# 1 / 1


def fall(k):
    sy, sx, h, w = infos[k]
    belows = [[sy + h - 1, sx + x] for x in range(w)]

    cnt = 0
    while belows[0][0] + 1 + cnt !=  N:
        for ii in range(len(belows)):
            y, x = belows[ii]
            if area[y + 1 + cnt][x]:
                break
        else:
            cnt += 1
            continue
        break

    if cnt:
        for y in range(sy, sy + h):
            for x in range(sx, sx + w):
                area[y][x] = 0
        for y in range(sy, sy + h):
            for x in range(sx, sx + w):
                area[y + cnt][x] = k
        infos[k][0] += cnt

    return cnt


def put_box(k, h, w, c):
    for y in range(h):
        for x in range(w):
            area[y][c - 1 + x] = k
    infos[k] = [0, c - 1, h, w]
    fall(k)


def check_left():
    for n in range(1, 101):
        if infos[n][0] == -1:
            continue

        sy, sx, h, w = infos[n]
        lefts = [[sy + dy, sx] for dy in range(h)]
        poss = True

        while lefts[0][1] != 0:
            for l in range(len(lefts)):
                y, x = lefts[l]
                if area[y][x - 1]:
                    poss = False
                    break
                lefts[l][1] -= 1
            else:
                continue
            break

        if poss:
            return n


def check_right():
    for n in range(1, 101):
        if infos[n][0] == -1:
            continue

        sy, sx, h, w = infos[n]
        rights = [[sy + dy, sx + w - 1] for dy in range(h)]
        poss = True

        while rights[0][1] != N - 1:
            for r in range(len(rights)):
                y, x = rights[r]
                if area[y][x + 1]:
                    poss = False
                    break
                rights[r][1] += 1
            else:
                continue
            break

        if poss:
            return n


def check_fall():
    checked = {0}

    for y in range(N - 1, -1, -1):
        for x in range(N):
            if area[y][x] in checked:
                continue
            fall(area[y][x])


N, M = map(int, input().split())
area = [[0] * N for _ in range(N)]
infos = [[-1] for _ in range(101)]
for i in range(M):
    kk, hh, ww, cc = map(int, input().split())
    put_box(kk, hh, ww, cc)

for i in range(M):
    if i % 2 == 0:
        kk = check_left()
    else:
        kk = check_right()

    print(kk)

    si, sj, hh, ww = infos[kk]
    for ii in range(si, si + hh):
        for jj in range(sj, sj + ww):
            area[ii][jj] = 0
    infos[kk][0] = -1

    check_fall()
