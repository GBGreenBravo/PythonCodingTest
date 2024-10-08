# 20241008
# 1:31:01
# 1 / 1

# 비겼을 때, 지우/경희/민호 순으로 비교하지 않고,
# 이전 가위바위보 승자 / 새로 들어온 사람 으로 생각해서, 꼬였던 문제

# 추가로, 경희/민호의 값은 매번 deepcopy하지 말고, pointer로만 관리했어도 좋았을 듯.

# win_lst = 0:지우 / 1:경희 / 2:민호
def dfs(recent_winner, next_fighter, win_lst, recent_used, k_remain, m_remain):
    global win_possible

    if win_possible:
        return

    if max(win_lst) == k:
        if win_lst[0] == k:
            win_possible = True
        return

    if recent_winner == 0:
        options = list(range(n))
        for used in recent_used:
            options.remove(used)
        if not options:
            return
        if next_fighter == 1:
            for option in options:
                before, after = option, k_remain[0]
                if before == after:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[1] += 1
                    dfs(1, 2, next_win_lst, [rr for rr in recent_used] + [option], [kk for kk in k_remain][1:], m_remain)
                elif wld[before][after] == 2:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[0] += 1
                    dfs(0, 2, next_win_lst, [rr for rr in recent_used] + [option], [kk for kk in k_remain][1:], m_remain)
                else:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[1] += 1
                    dfs(1, 2, next_win_lst, [rr for rr in recent_used] + [option], [kk for kk in k_remain][1:], m_remain)
        elif next_fighter == 2:
            for option in options:
                before, after = option, m_remain[0]
                if before == after:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[2] += 1
                    dfs(2, 1, next_win_lst, [rr for rr in recent_used] + [option], k_remain, [mm for mm in m_remain][1:])
                elif wld[before][after] == 2:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[0] += 1
                    dfs(0, 1, next_win_lst, [rr for rr in recent_used] + [option], k_remain, [mm for mm in m_remain][1:])
                else:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[2] += 1
                    dfs(2, 1, next_win_lst, [rr for rr in recent_used] + [option], k_remain, [mm for mm in m_remain][1:])

    elif recent_winner == 1:
        if next_fighter == 0:
            options = list(range(n))
            for used in recent_used:
                options.remove(used)
            if not options:
                return
            for option in options:
                before, after = k_remain[0], option
                if before == after:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[1] += 1
                    dfs(1, 2, next_win_lst, [rr for rr in recent_used] + [option], [kk for kk in k_remain][1:], [mm for mm in m_remain])
                elif wld[before][after] == 2:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[1] += 1
                    dfs(1, 2, next_win_lst, [rr for rr in recent_used] + [option], [kk for kk in k_remain][1:], [mm for mm in m_remain])
                else:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[0] += 1
                    dfs(0, 2, next_win_lst, [rr for rr in recent_used] + [option], [kk for kk in k_remain][1:], [mm for mm in m_remain])
        elif next_fighter == 2:
            before, after = k_remain[0], m_remain[0]
            if before == after:
                next_win_lst = [ww for ww in win_lst]
                next_win_lst[2] += 1
                dfs(2, 0, next_win_lst, [rr for rr in recent_used], [kk for kk in k_remain][1:], [mm for mm in m_remain][1:])
            elif wld[before][after] == 2:
                next_win_lst = [ww for ww in win_lst]
                next_win_lst[1] += 1
                dfs(1, 0, next_win_lst, [rr for rr in recent_used], [kk for kk in k_remain][1:], [mm for mm in m_remain][1:])
            else:
                next_win_lst = [ww for ww in win_lst]
                next_win_lst[2] += 1
                dfs(2, 0, next_win_lst, [rr for rr in recent_used], [kk for kk in k_remain][1:], [mm for mm in m_remain][1:])

    elif recent_winner == 2:
        if next_fighter == 0:
            options = list(range(n))
            for used in recent_used:
                options.remove(used)
            if not options:
                return
            for option in options:
                before, after = m_remain[0], option
                if before == after:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[2] += 1
                    dfs(2, 1, next_win_lst, [rr for rr in recent_used] + [option], [kk for kk in k_remain], [mm for mm in m_remain][1:])
                elif wld[before][after] == 2:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[2] += 1
                    dfs(2, 1, next_win_lst, [rr for rr in recent_used] + [option], [kk for kk in k_remain], [mm for mm in m_remain][1:])
                else:
                    next_win_lst = [ww for ww in win_lst]
                    next_win_lst[0] += 1
                    dfs(0, 1, next_win_lst, [rr for rr in recent_used] + [option], [kk for kk in k_remain], [mm for mm in m_remain][1:])
        elif next_fighter == 1:
            before, after = m_remain[0], k_remain[0]
            if before == after:
                next_win_lst = [ww for ww in win_lst]
                next_win_lst[2] += 1
                dfs(2, 0, next_win_lst, [rr for rr in recent_used], [kk for kk in k_remain][1:], [mm for mm in m_remain][1:])
            elif wld[before][after] == 2:
                next_win_lst = [ww for ww in win_lst]
                next_win_lst[2] += 1
                dfs(2, 0, next_win_lst, [rr for rr in recent_used], [kk for kk in k_remain][1:], [mm for mm in m_remain][1:])
            else:
                next_win_lst = [ww for ww in win_lst]
                next_win_lst[1] += 1
                dfs(1, 0, next_win_lst, [rr for rr in recent_used], [kk for kk in k_remain][1:], [mm for mm in m_remain][1:])


n, k = map(int, input().split())
wld = [tuple(map(int, input().split())) for _ in range(n)]  # 2: 앞이 이김 / 1: 비김 / 0: 뒤가 이김
kyunghee = list(map(lambda inp: int(inp) - 1, input().split()))
minho = list(map(lambda inp: int(inp) - 1, input().split()))


win_possible = False
dfs(0, 1, [0, 0, 0], [], [kk for kk in kyunghee], [mm for mm in minho])
print(int(win_possible))
