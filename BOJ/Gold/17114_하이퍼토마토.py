# 20240811
# 32:24
# 1 / 1

from collections import deque

m, n, o, p, q, r, s, t, u, v, w = map(int, input().split())
arr = [[[[[[[[[[[0] * m for _ in range(n)] for _ in range(o)] for _ in range(p)] for _ in range(q)] for _ in range(r)] for _ in range(s)] for _ in range(t)] for _ in range(u)] for _ in range(v)] for _ in range(w)]

for ww in range(w):
    for vv in range(v):
        for uu in range(u):
            for tt in range(t):
                for ss in range(s):
                    for rr in range(r):
                        for qq in range(q):
                            for pp in range(p):
                                for oo in range(o):
                                    for nn in range(n):
                                        arr[ww][vv][uu][tt][ss][rr][qq][pp][oo][nn] = list(map(int, input().split()))

visited = [[[[[[[[[[[0] * m for _ in range(n)] for _ in range(o)] for _ in range(p)] for _ in range(q)] for _ in range(r)] for _ in range(s)] for _ in range(t)] for _ in range(u)] for _ in range(v)] for _ in range(w)]
queue = deque()

for ww in range(w):
    for vv in range(v):
        for uu in range(u):
            for tt in range(t):
                for ss in range(s):
                    for rr in range(r):
                        for qq in range(q):
                            for pp in range(p):
                                for oo in range(o):
                                    for nn in range(n):
                                        for mm in range(m):
                                            if arr[ww][vv][uu][tt][ss][rr][qq][pp][oo][nn][mm] == 1:
                                                queue.append((ww, vv, uu, tt, ss, rr, qq, pp, oo, nn, mm))
                                                visited[ww][vv][uu][tt][ss][rr][qq][pp][oo][nn][mm] = 1

direction = ((1,0,0,0,0,0,0,0,0,0,0), (-1,0,0,0,0,0,0,0,0,0,0),
             (0,1,0,0,0,0,0,0,0,0,0), (0,-1,0,0,0,0,0,0,0,0,0),
             (0,0,1,0,0,0,0,0,0,0,0), (0,0,-1,0,0,0,0,0,0,0,0),
             (0,0,0,1,0,0,0,0,0,0,0), (0,0,0,-1,0,0,0,0,0,0,0),
             (0,0,0,0,1,0,0,0,0,0,0), (0,0,0,0,-1,0,0,0,0,0,0),
             (0,0,0,0,0,1,0,0,0,0,0), (0,0,0,0,0,-1,0,0,0,0,0),
             (0,0,0,0,0,0,1,0,0,0,0), (0,0,0,0,0,0,-1,0,0,0,0),
             (0,0,0,0,0,0,0,1,0,0,0), (0,0,0,0,0,0,0,-1,0,0,0),
             (0,0,0,0,0,0,0,0,1,0,0), (0,0,0,0,0,0,0,0,-1,0,0),
             (0,0,0,0,0,0,0,0,0,1,0), (0,0,0,0,0,0,0,0,0,-1,0),
             (0,0,0,0,0,0,0,0,0,0,1), (0,0,0,0,0,0,0,0,0,0,-1))


def oob(ccw, ccv, ccu, cct, ccs, ccr, ccq, ccp, cco, ccn, ccm):
    return (not(0 <= ccw < w)
            or not(0 <= ccv < v)
            or not(0 <= ccu < u)
            or not(0 <= cct < t)
            or not(0 <= ccs < s)
            or not(0 <= ccr < r)
            or not(0 <= ccq < q)
            or not(0 <= ccp < p)
            or not(0 <= cco < o)
            or not(0 <= ccn < n)
            or not(0 <= ccm < m))


while queue:
    cw, cv, cu, ct, cs, cr, cq, cp, co, cn, cm = queue.popleft()
    for dw, dv, du, dt, ds, dr, dq, dp, do, dn, dm in direction:
        nw, nv, nu, nt, ns, nr, nq, np, no, nn, nm = cw + dw, cv + dv, cu + du, ct + dt, cs + ds, cr + dr, cq + dq, cp + dp, co + do, cn + dn, cm + dm
        if oob(nw, nv, nu, nt, ns, nr, nq, np, no, nn, nm):
            continue
        if visited[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm]:
            continue
        if arr[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] == -1:
            continue
        visited[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = visited[cw][cv][cu][ct][cs][cr][cq][cp][co][cn][cm] + 1
        queue.append((nw, nv, nu, nt, ns, nr, nq, np, no, nn, nm))

answer = 1
not_all = False
for ww in range(w):
    for vv in range(v):
        for uu in range(u):
            for tt in range(t):
                for ss in range(s):
                    for rr in range(r):
                        for qq in range(q):
                            for pp in range(p):
                                for oo in range(o):
                                    for nn in range(n):
                                        for mm in range(m):
                                            if arr[ww][vv][uu][tt][ss][rr][qq][pp][oo][nn][mm] == -1:
                                                continue
                                            if visited[ww][vv][uu][tt][ss][rr][qq][pp][oo][nn][mm] == 0:
                                                not_all = True
                                                break
                                            answer = max(answer, visited[ww][vv][uu][tt][ss][rr][qq][pp][oo][nn][mm])

print(-1 if not_all else answer - 1)
