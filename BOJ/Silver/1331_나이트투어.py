# 20240819
# 14:00
# 1 / 1

# visited 체크하는 반복문을 따로 구성할 필요는 없었고, 뒤의 else 안에 있는 반복문에서 처리해줬다면, 시간복잡도 더 낮았음.


def convert_to_indexes(str_move):
    alpha, num = str_move
    alpha = ord(alpha) - ord("A")
    num = int(num) - 1
    return alpha, num


moves = [str(input()) for _ in range(36)]
for i in range(36):
    moves[i] = convert_to_indexes(moves[i])  # 체스판 형식의 좌표를 숫자형 좌표(y, x)로 변경

visited = [[False] * 6 for _ in range(6)]
for my, mx in moves:
    visited[my][mx] = True
if sum(map(sum, visited)) != 36:  # 문제에서 체스판의 다른 좌표 36개가 모두 들어온다고 명시 안 되어 있어, 한 좌표라도 중복되면 Invalid
    print("Invalid")
else:
    is_valid = True
    y, x = moves[0]
    for i in range(1, 36):
        ny, nx = moves[i]
        if tuple(sorted([abs(y - ny), abs(x - nx)])) != (1, 2):  # 좌표간 거리가 (1, 2)로 구성 안 된다면, Invalid
            is_valid = False
            break
        y, x = ny, nx
    if tuple(sorted([abs(y - moves[0][0]), abs(x - moves[0][1])])) != (1, 2):  # 마지막 좌표와 첫 좌표 거리도 비교
        is_valid = False
    print("Valid" if is_valid else "Invalid")
