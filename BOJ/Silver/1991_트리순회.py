# 20240805
# 12:27
# 1 / 1


def pre_order(alphabet):
    left, right = connected[alpha_to_index[alphabet]]
    print(alphabet, end="")
    if left:
        pre_order(left)
    if right:
        pre_order(right)


def in_order(alphabet):
    left, right = connected[alpha_to_index[alphabet]]
    if left:
        in_order(left)
    print(alphabet, end="")
    if right:
        in_order(right)


def post_order(alphabet):
    left, right = connected[alpha_to_index[alphabet]]
    if left:
        post_order(left)
    if right:
        post_order(right)
    print(alphabet, end="")


n = int(input())
alpha_to_index = dict()
connected = [[None, None] for _ in range(n)]

for i in range(n):
    parent, left, right = map(str, input().split())

    alpha_to_index[parent] = i

    if left != '.':
        connected[i][0] = left
    if right != '.':
        connected[i][1] = right

pre_order('A')
print()
in_order('A')
print()
post_order('A')
