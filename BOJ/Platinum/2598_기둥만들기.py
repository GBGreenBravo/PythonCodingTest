# 20241210
# 53:56
# 1 / 2

fixed_sides = ((1, 5, 3, 4),
               (0, 4, 2, 5),
               (1, 4, 3, 5),
               (0, 5, 2, 4),
               (0, 3, 2, 1),
               (0, 1, 2, 3))
opposite_side = (2, 3, 0, 1, 5, 4)


def check():
    for dice1_bottom in range(6):
        dice1_sides = [dices[0][i] for i in fixed_sides[dice1_bottom]]
        for dice2_bottom in range(6):
            for r2 in range(4):
                dice2_sides = [dices[1][i] for i in fixed_sides[dice2_bottom]]
                dice2_sides = dice2_sides[r2:] + dice2_sides[:r2]
                for dice3_bottom in range(6):
                    for r3 in range(4):
                        dice3_sides = [dices[2][i] for i in fixed_sides[dice3_bottom]]
                        dice3_sides = dice3_sides[r3:] + dice3_sides[:r3]
                        for dice4_bottom in range(6):
                            for r4 in range(4):
                                dice4_sides = [dices[3][i] for i in fixed_sides[dice4_bottom]]
                                dice4_sides = dice4_sides[r4:] + dice4_sides[:r4]
                                first = (dice1_sides[0], dice2_sides[0], dice3_sides[0], dice4_sides[0])
                                second = (dice1_sides[1], dice2_sides[1], dice3_sides[1], dice4_sides[1])
                                third = (dice1_sides[2], dice2_sides[2], dice3_sides[2], dice4_sides[2])
                                fourth = (dice1_sides[3], dice2_sides[3], dice3_sides[3], dice4_sides[3])
                                if len(set(first)) != 4 or len(set(second)) != 4 or len(set(third)) != 4 or len(set(fourth)) != 4:
                                    continue
                                c1 = (dices[3][opposite_side[dice4_bottom]],) + first + second + third + fourth
                                c2 = (dices[3][opposite_side[dice4_bottom]],) + second + third + fourth + first
                                c3 = (dices[3][opposite_side[dice4_bottom]],) + third + fourth + first + second
                                c4 = (dices[3][opposite_side[dice4_bottom]],) + fourth + first + second + third
                                set_c = set([c1, c2, c3, c4])
                                if len(set_c) == 1:
                                    answers1.update(set_c)
                                elif len(set_c) == 2:
                                    answers2.update(set_c)
                                else:
                                    answers4.update(set_c)


def dfs(cnt):
    if cnt == 4:
        check()
        return

    for idx in range(4):
        if idx not in dfs_arr:
            dfs_arr.append(idx)
            dfs(cnt + 1)
            dfs_arr.pop()


dices = [list(str(input())) for _ in range(4)]
answers4 = set()
answers2 = set()
answers1 = set()
dfs_arr = []
dfs(0)
print(len(answers1) + len(answers2) // 2 + len(answers4) // 4)
