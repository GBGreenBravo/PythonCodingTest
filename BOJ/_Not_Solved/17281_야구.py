# from collections import deque
#
#
# def play_ball():
#     score = 0
#     order_idx = 0
#
#     for inning in range(n):
#         remained_out_cnt = 3
#         bases = deque()
#         bases.extend([0, 0, 0])
#
#         while remained_out_cnt:
#             now_hit = hits[inning][player_order[order_idx % 9]]
#
#             if now_hit == 0:
#                 remained_out_cnt -= 1
#             elif now_hit == 1:
#                 bases.append(1)
#             elif now_hit == 2:
#                 bases.extend([1, 0])
#             elif now_hit == 3:
#                 bases.extend([1, 0, 0])
#             elif now_hit == 4:
#                 bases.extend([1, 0, 0, 0])
#
#             order_idx += 1
#
#         for _ in range(3):
#             bases.pop()
#
#         score += sum(bases)
#
#     global mx
#     if score > mx:
#         mx = score


# def play_ball():
#     score = 0
#     order_idx = 0
#
#     for inning in range(n):
#         remained_out_cnt = 3
#         bases = 0
#
#         while remained_out_cnt:
#             now_hit = hits[inning][player_order[order_idx]]
#
#             if now_hit == 0:
#                 remained_out_cnt -= 1
#             elif now_hit == 1:
#                 bases <<= 1
#                 bases += 1
#             elif now_hit == 2:
#                 bases <<= 1
#                 bases += 1
#                 bases <<= 1
#             elif now_hit == 3:
#                 bases <<= 1
#                 bases += 1
#                 bases <<= 2
#             elif now_hit == 4:
#                 bases <<= 1
#                 bases += 1
#                 bases <<= 3
#
#             order_idx += 1
#             order_idx %= 9
#
#         bases >>= 3
#         # while bases:
#         #     score += bases & 1
#         #     bases >>= 1
#         score += str(bin(bases)).count('1')
#
#     global mx
#     if score > mx:
#         mx = score


# def play_ball():
#     score = 0
#     order_idx = 0
#
#     for inning in range(n):
#         remained_out_cnt = 3
#         bases = []
#
#         while remained_out_cnt:
#             now_hit = hits[inning][player_order[order_idx]]
#
#             if now_hit == 0:
#                 remained_out_cnt -= 1
#                 order_idx += 1
#                 order_idx %= 9
#                 continue
#             elif now_hit == 1:
#                 bases.append(1)
#             elif now_hit == 2:
#                 bases.append(2)
#             elif now_hit == 3:
#                 bases.append(3)
#             else:  # elif now_hit == 4:
#                 bases.append(4)
#
#             order_idx += 1
#             order_idx %= 9
#
#         homes = len(bases)
#         if not homes:
#             continue
#         score += len(bases[:-3])
#
#         if len(bases) >= 3:
#             if bases[-1] == 4:
#                 score += 3
#             if bases[-1] == 3:
#                 score += 2
#             elif bases[-1] == 2:
#                 if bases[-2] > 1:
#                     score += 2
#                 else:
#                     score += 1
#             elif bases[-1] == 1:
#                 if bases[-2] > 2:
#                     score += 2
#                 elif bases[-2] == 2:
#                     score += 1
#                 elif bases[-2] == 1:
#                     if bases[-3] > 1:
#                         score += 1
#         elif len(bases) == 2:
#             if bases[-1] == 4:
#                 score += 2
#             if bases[-1] == 3:
#                 score += 1
#             elif bases[-1] == 2:
#                 if bases[-2] > 1:
#                     score += 1
#             elif bases[-1] == 1:
#                 if bases[-2] > 2:
#                     score += 1
#         elif len(bases) == 1:
#             if bases[-1] == 4:
#                 score += 1
#
#     global mx
#     if score > mx:
#         mx = score


# def play_ball():
#     score = 0
#     order_idx = 0
#
#     inning = 0
#     remained_out_cnt = 3 * n
#
#     bases = []
#
#     while inning != n:
#         now_hit = hits[inning][player_order[order_idx]]
#
#         if now_hit == 0:
#             remained_out_cnt -= 1
#             if remained_out_cnt % 3 == 0:
#                 inning += 1
#                 score += bases[:-3].count(1)
#                 bases = []
#         elif now_hit == 1:
#             bases.append(1)
#         elif now_hit == 2:
#             bases.extend([1, 0])
#         elif now_hit == 3:
#             bases.extend([1, 0, 0])
#         else:  # elif now_hit == 4:
#             bases.extend([1, 0, 0, 0])
#
#         order_idx += 1
#         order_idx %= 9
#
#     global mx
#     if score > mx:
#         mx = score


# def play_ball():
#     score = 0
#     order_idx = 0
#
#     for inning in range(n):
#         remained_out_cnt = 3
#         bases = 0
#
#         while remained_out_cnt:
#             now_hit = hits[inning][player_order[order_idx]]
#
#             if now_hit == 0:
#                 remained_out_cnt -= 1
#             elif now_hit == 1:
#                 bases <<= 1
#                 bases += 1
#             elif now_hit == 2:
#                 bases <<= 1
#                 bases += 1
#                 bases <<= 1
#             elif now_hit == 3:
#                 score += str(bin(bases)).count('1')
#                 bases = 4
#             elif now_hit == 4:
#                 score += str(bin(bases)).count('1') + 1
#                 bases = 0
#
#             order_idx += 1
#             order_idx %= 9
#
#         bases >>= 3
#         score += str(bin(bases)).count('1')
#
#     global mx
#     if score > mx:
#         mx = score


def arrange_players(cnt):
    if cnt == 9:
        play_ball()
        return

    if cnt == 3:
        player_order.append(0)
        arrange_players(4)
        player_order.pop()

    for i in range(1, 9):
        if i in visited:
            continue

        player_order.append(i)
        visited.add(i)
        arrange_players(cnt + 1)
        visited.remove(i)
        player_order.pop()


n = int(input())
hits = [tuple(map(int, input().split())) for _ in range(n)]

mx = 0
player_order = []
visited = set()
arrange_players(0)
print(mx)
