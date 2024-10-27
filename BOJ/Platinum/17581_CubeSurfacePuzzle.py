# 20241027
# 2:21:48
# 1 / 4

# 처음 제출했던 코드도 로직은 틀리지 않았지만,
# 이진수&비트연산자를 활용해서 연산 횟수를 줄여야했던 문제.

# 주요 로직:
#   윗면은 처음에 들어오는 면으로 고정해놓고, 한번 뒤집기만 함. (2)
#   나머지 5면들은 회전/뒤집기 다 해주면 면 당 (8)가지 경우가 생김.
#   그러면 (주사위 면 구성하는) 5! * (면 당 경우의 수) 2**1 * 8**5 로 시간복잡도 계산됨. => 7864320
#   (이진수&비트연산자를 활용하지 않으면, 위 복잡도에 4N+a가 곱해지기에 시간초과 가능.)
#   면 6개와 모서리 12개에 대해, 임의의 index와 방향을 지정하고 모서리 더해주면 됨.

up = (1, 9, 0, 3, 2, 1)
left = (0, 8, 4, 7, 5, 4)
right = (2, 10, 7, 6, 6, 5)
down = (3, 11, 8, 11, 10, 9)
other_edge = (((4, 0), (5, 0), (6, 0), (7, 0)),
              ((4, -1), (5, -1), (6, -1), (7, -1)),
              ((1, 0), (3, 0), (11, 0), (9, 0)),
              ((0, -1), (2, -1), (10, -1), (8, -1)),
              ((1, -1), (3, -1), (11, -1), (9, -1)),
              ((0, 0), (2, 0), (10, 0), (8, 0)))


def fill_edges(edges_arr, face_index, area):
    new_edges = [e for e in edges_arr]
    if area[0] & 2**(N-1):
        new_edges[other_edge[face_index][0][0]] += 2**(N-1) if other_edge[face_index][0][1] == 0 else 1
    if area[0] & 1:
        new_edges[other_edge[face_index][1][0]] += 2**(N-1) if other_edge[face_index][1][1] == 0 else 1
    if area[3] & 1:
        new_edges[other_edge[face_index][2][0]] += 2**(N-1) if other_edge[face_index][2][1] == 0 else 1
    if area[3] & 2**(N-1):
        new_edges[other_edge[face_index][3][0]] += 2**(N-1) if other_edge[face_index][3][1] == 0 else 1
    new_edges[up[face_index]] += area[0]
    new_edges[left[face_index]] += area[1]
    new_edges[right[face_index]] += area[2]
    new_edges[down[face_index]] += area[3]

    if max(new_edges) >= 2**N:
        return False
    else:
        return new_edges


def final_check(edges_arr):
    for edge in edges_arr:
        if edge != 2 ** N - 1:
            return False
    return True


def dfs(cnt):
    global possible

    if possible:
        return

    if cnt == 6:
        edges = [0] * 12

        for a0 in areas[dfs_arr[0]]:
            edges0 = fill_edges(edges, 0, a0)

            for a1 in areas[dfs_arr[1]]:
                edges1 = fill_edges(edges0, 1, a1)
                if not edges1:
                    continue

                for a2 in areas[dfs_arr[2]]:
                    edges2 = fill_edges(edges1, 2, a2)
                    if not edges2:
                        continue

                    for a3 in areas[dfs_arr[3]]:
                        edges3 = fill_edges(edges2, 3, a3)
                        if not edges3:
                            continue

                        for a4 in areas[dfs_arr[4]]:
                            edges4 = fill_edges(edges3, 4, a4)
                            if not edges4:
                                continue

                            for a5 in areas[dfs_arr[5]]:
                                edges5 = fill_edges(edges4, 5, a5)
                                if not edges5 or not final_check(edges5):
                                    continue
                                possible = True
                                break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break

        return

    for idx in range(1, 6):
        if idx not in dfs_arr:
            dfs_arr.append(idx)
            dfs(cnt + 1)
            dfs_arr.pop()


while True:
    N = int(input())
    if not N:
        break
    areas = []
    for _ in range(6):
        areas.append([[[int(inp == 'X') for inp in str(input())] for _ in range(N)]])

    for i in range(6):
        areas[i][0] = [areas[i][0][0],
                       [a[0] for a in areas[i][0]],
                       [a[-1] for a in areas[i][0]],
                       areas[i][0][-1]]
        if i:
            for _ in range(3):
                areas[i].append([areas[i][-1][1][::-1], areas[i][-1][3][:], areas[i][-1][0][:], areas[i][-1][2][::-1]])
        areas[i].append([areas[i][0][3][:], areas[i][0][1][::-1], areas[i][0][2][::-1], areas[i][0][0][:]])
        if i:
            for _ in range(3):
                areas[i].append([areas[i][-1][1][::-1], areas[i][-1][3][:], areas[i][-1][0][:], areas[i][-1][2][::-1]])
        for j in range(len(areas[i])):
            for k in range(4):
                now_bin = 0
                for bin_idx, value in enumerate(areas[i][j][k][::-1]):
                    now_bin += 2**bin_idx * value
                areas[i][j][k] = now_bin

    possible = False
    dfs_arr = [0]
    dfs(1)

    print("Yes" if possible else "No")
