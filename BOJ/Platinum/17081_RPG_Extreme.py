# 20241206
# 1:30:01
# 1 / 2

direction = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def thorn_damage():
    global now_hp
    now_hp -= 1 if "DX" in accessories else 5


def fight_with(ay, ax):
    global now_hp, now_experience, level, max_hp, offence, defence

    if area[ay][ax] == 'M' and "HU" in accessories:
        now_hp = max_hp

    _, a_offense, a_defence, a_hp, a_experience = monsters[(ay, ax)]

    t = 1
    while True:
        if t == 1 and "CO" in accessories:
            if "DX" in accessories:
                a_hp -= max(1, (offence + weapon) * 3 - a_defence)
            else:
                a_hp -= max(1, (offence + weapon) * 2 - a_defence)
        else:
            a_hp -= max(1, (offence + weapon) - a_defence)
        if a_hp <= 0:
            break
        if t == 1 and area[ay][ax] == 'M' and "HU" in accessories:
            t += 1
            continue
        now_hp -= max(1, a_offense - (defence + armor))
        if now_hp <= 0:
            return
        t += 1
    if "EX" in accessories:
        now_experience += int(1.2 * a_experience)
    else:
        now_experience += a_experience
    if now_experience >= 5 * level:
        level += 1
        now_experience = 0
        max_hp += 5
        offence += 2
        defence += 2
        now_hp = max_hp
    if "HR" in accessories:
        now_hp = min(max_hp, now_hp + 3)


def print_status():
    global now_hp

    if now_hp <= 0:
        now_hp = 0
    else:
        area[main_y][main_x] = '@'
    for a in area:
        print(*a, sep="")
    print("Passed Turns : " + str(turn + 1))
    print("LV : " + str(level))
    print("HP : " + str(now_hp) + "/" + str(max_hp))
    print("ATT : " + str(offence) + "+" + str(weapon))
    print("DEF : " + str(defence) + "+" + str(armor))
    print("EXP : " + str(now_experience) + "/" + str(5 * level))


N, M = map(int, input().split())
area = [list(str(input())) for _ in range(N)]
moves = list(str(input()))

monsters = dict()
for _ in range(sum(map(lambda row: row.count('&'), area)) + 1):
    yy, xx, ss, ww, aa, hh, ee = input().split()
    monsters[(int(yy) - 1, int(xx) - 1)] = [ss, int(ww), int(aa), int(hh), int(ee)]

items = dict()
for _ in range(sum(map(lambda row: row.count('B'), area))):
    yy, xx, tt, ss = input().split()
    items[(int(yy) - 1, int(xx) - 1)] = [tt, ss]

for i in range(N):
    for j in range(M):
        if area[i][j] == '@':
            si, sj = i, j
            area[i][j] = '.'

main_y, main_x = si, sj
now_hp, max_hp, offence, defence = 20, 20, 2, 2
level, now_experience = 1, 0
weapon, armor, accessories = 0, 0, set()

for turn, m in enumerate(moves):
    dy, dx = direction[m]
    ny, nx = main_y + dy, main_x + dx

    if oob(ny, nx) or area[ny][nx] == '#':
        if area[main_y][main_x] == '^':
            thorn_damage()
            if now_hp <= 0:
                if "RE" in accessories:
                    accessories.remove("RE")
                    main_y, main_x = si, sj
                    now_hp = max_hp
                    continue
                print_status()
                print("YOU HAVE BEEN KILLED BY SPIKE TRAP..")
                break
        continue

    nex = area[ny][nx]
    if nex == '.':
        main_y, main_x = ny, nx

    elif nex == 'B':
        sort, detail = items[(ny, nx)]
        if sort == 'W':
            weapon = int(detail)
        elif sort == 'A':
            armor = int(detail)
        elif sort == 'O':
            if len(accessories) < 4 and detail not in accessories:
                accessories.add(detail)
        area[ny][nx] = '.'
        main_y, main_x = ny, nx

    elif nex == '^':
        main_y, main_x = ny, nx
        thorn_damage()
        if now_hp <= 0:
            if "RE" in accessories:
                accessories.remove("RE")
                main_y, main_x = si, sj
                now_hp = max_hp
                continue
            print_status()
            print("YOU HAVE BEEN KILLED BY SPIKE TRAP..")
            break

    elif nex == "M":
        m_name = monsters[(ny, nx)][0]
        fight_with(ny, nx)
        if now_hp <= 0:
            if "RE" in accessories:
                accessories.remove("RE")
                main_y, main_x = si, sj
                now_hp = max_hp
                continue
            print_status()
            print("YOU HAVE BEEN KILLED BY " + m_name + '..')
            break
        else:
            main_y, main_x = ny, nx
            print_status()
            print("YOU WIN!")
            break

    else:
        m_name = monsters[(ny, nx)][0]
        fight_with(ny, nx)
        if now_hp <= 0:
            if "RE" in accessories:
                accessories.remove("RE")
                main_y, main_x = si, sj
                now_hp = max_hp
                continue
            print_status()
            print("YOU HAVE BEEN KILLED BY " + m_name + '..')
            break
        area[ny][nx] = '.'
        main_y, main_x = ny, nx


else:
    print_status()
    print("Press any key to continue.")
