# 20240814
# 14:09
# 1 / 2

n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)  # 절단 가능한 나무길이의 최소값과 최대값; 최대값을 max(trees)로 설정하면, m이 1인 경우에 오답을 도출함.
while left < right:  # 이분탐색
    mid = (left + right) // 2
    # mid_value = sum([tree - mid for tree in trees if tree - mid > 0])
    mid_value = 0  # 위 코드로 간편하게 절단후 얻는 나무길이를 구할 수 있었지만, sum() 때문에 trees길이만큼 연산이 더 추가되어 시간 소모가 컸다.
    for tree in trees:
        if tree > mid:
            mid_value += tree - mid

    if mid_value == m:
        left = mid + 1
        break
    elif mid_value < m:
        right = mid
    elif mid_value > m:
        left = mid + 1

print(
    left - 1)  # 이분탐색의 종료조건이 left < right라서, left == right이거나 m을 찾을 때 종료되는데, 종료 전의 left의 절단값은 항상 m보다 크거나 같았고, 종료 직전에 +1 되었기에, 출력에서는 -1을 해준다.


# while문 조건을 left <= right 로 작성한 코드
"""
n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)
while left <= right:
    mid = (left + right) // 2
    mid_value = 0
    for tree in trees:
        if tree > mid:
            mid_value += tree - mid

    if mid_value == m:
        right = mid
        break
    elif mid_value < m:
        right = mid - 1
    elif mid_value > m:
        left = mid + 1

print(right)  # 반복문 내에서의 right는 항상 value가 m보다 작았지만, 종료(m 찾거나, left==right)후의 right value는 m이상이 되게 된다.
"""


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
