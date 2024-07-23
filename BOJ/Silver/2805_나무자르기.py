# 20240723
# 14:45

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)


def cut(trees_1, length):
    cut_trees = 0
    for tree in trees_1:
        if tree <= length:
            break
        else:
            cut_trees += tree - length
    return cut_trees


up, down = trees[0], 0
while up != down:
    now_height = (up + down) // 2 + 1
    now_trees = cut(trees, now_height)
    if now_trees < m:
        up = now_height - 1
        continue
    else:
        down = now_height

print(up)


# 이분탐색 문제였음.
# 위 풀이는 시간복잡도 O(NlogN + NlogH)였음. sort() 안 쓰고 한다면 O(NlogH)만으로도 가능.
