# 20240812
# 1:54:30
# 1 / 6

# 15번째 줄의 코드에서 num == 2로 처리했어서, n이 1인 케이스에 대해 에러가 떴음.
# 그러나, 해당 이슈를 인지하지 못하고 계속 코드만 의심했음. 기본적인 테케도 안 돌린 나를 의심하자.

import sys
sys.setrecursionlimit(40_000)


def move_arr_a_to_b(num, a, b):
    global answer_cnt, answer_route
    c = [i for i in range(1, 4) if i not in [a, b]][0]
    if num == 1:
        answer_cnt += 1
        answer_route.append((a, b))
        return
    move_arr_a_to_b(num - 1, a, c)
    answer_cnt += 1
    answer_route.append((a, b))
    move_arr_a_to_b(num - 1, c, b)


n = int(input())
answer_cnt = 0
answer_route = []
move_arr_a_to_b(n, 1, 3)

print(answer_cnt)
for route in answer_route:
    print(*route)


# 아래는 BFS 활용했던 처음 풀이. 20 입력했을 때, 시간 1초보다 오래 걸려서 이 방식은 아님을 인지.
"""
from collections import deque


def make_tuple(rods_arr):
    return tuple(tuple([i for i in arr]) for arr in rods_arr)


def bfs(rods_arr):
    queue = deque()
    queue.append((rods_arr, 0, []))
    visited = set()
    visited.add(make_tuple)

    while queue:
        now_arr, cnt, history = queue.popleft()
        if make_tuple(now_arr) == (tuple(), tuple(), tuple(i for i in range(1, n + 1))):
            return cnt, history
        # 1에서 2,3
        if now_arr[0]:
            peek_1 = now_arr[0][0]
            if not now_arr[1] or (now_arr[1] and peek_1 < now_arr[1][0]):
                new_arr = [now_arr[0][1:], [peek_1] + now_arr[1], now_arr[2]]
                new_arr_tuple = make_tuple(new_arr)
                if new_arr_tuple not in visited:
                    visited.add(new_arr_tuple)
                    queue.append((new_arr, cnt + 1, history + [(1, 2)]))
            if not now_arr[2] or (now_arr[2] and peek_1 < now_arr[2][0]):
                new_arr = [now_arr[0][1:], now_arr[1], [peek_1] + now_arr[2]]
                new_arr_tuple = make_tuple(new_arr)
                if new_arr_tuple not in visited:
                    visited.add(new_arr_tuple)
                    queue.append((new_arr, cnt + 1, history + [(1, 3)]))
        # 2에서 1,3
        if now_arr[1]:
            peek_2 = now_arr[1][0]
            if not now_arr[0] or (now_arr[0] and peek_2 < now_arr[0][0]):
                new_arr = [[peek_2] + now_arr[0],  now_arr[1][1:], now_arr[2]]
                new_arr_tuple = make_tuple(new_arr)
                if new_arr_tuple not in visited:
                    visited.add(new_arr_tuple)
                    queue.append((new_arr, cnt + 1, history + [(2, 1)]))
            if not now_arr[2] or (now_arr[2] and peek_2 < now_arr[2][0]):
                new_arr = [now_arr[0],  now_arr[1][1:], [peek_2] + now_arr[2]]
                new_arr_tuple = make_tuple(new_arr)
                if new_arr_tuple not in visited:
                    visited.add(new_arr_tuple)
                    queue.append((new_arr, cnt + 1, history + [(2, 3)]))
        # 3에서 1,2
        if now_arr[2]:
            peek_3 = now_arr[2][0]
            if not now_arr[0] or (now_arr[0] and peek_3 < now_arr[0][0]):
                new_arr = [[peek_3] + now_arr[0],  now_arr[1], now_arr[2][1:]]
                new_arr_tuple = make_tuple(new_arr)
                if new_arr_tuple not in visited:
                    visited.add(new_arr_tuple)
                    queue.append((new_arr, cnt + 1, history + [(3, 1)]))
            if not now_arr[1] or (now_arr[1] and peek_3 < now_arr[1][0]):
                new_arr = [now_arr[0],  [peek_3] + now_arr[1], now_arr[2][1:]]
                new_arr_tuple = make_tuple(new_arr)
                if new_arr_tuple not in visited:
                    visited.add(new_arr_tuple)
                    queue.append((new_arr, cnt + 1, history + [(3, 2)]))


n = int(input())
rods = [[i for i in range(1, n + 1)], [], []]

answer_cnt, answer_history = bfs(rods)
print(answer_cnt)
for route in answer_history:
    print(*route)
"""