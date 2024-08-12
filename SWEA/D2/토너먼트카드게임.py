# 20240812
# 15:56
# 1 / 1


def rsp_winner(a, b):  # 늘 a_index가 b_index보다 작게 인자 받음.
    a_value, b_value = a[0], b[0]
    if a_value == b_value:  # a와 b가 비겼다면, 번호 작은 쪽(a) 승리
        return a

    if a_value == 1:  # a의 1만 4로 만들어준다면, a - 1 == b라면 a가 이기는 조합임.
        a_value += 3

    if a_value - 1 == b_value:  # a가 이긴다면
        return a
    else:  # b가 이긴다면
        return b


def rsp(arr):
    if len(arr) == 1:  # arr에 원소가 하나뿐이라면, 상대가 없으므로 원소 그대로 반환
        return arr[0]
    if len(arr) == 2:  # arr 길이가 2라면, 둘 중 승자 return
        return rsp_winner(arr[0], arr[1])

    middle = len(arr) // 2 if not len(arr) % 2 else len(arr) // 2 + 1  # 문제에서 요구하는 팀 선정. middle은 오른쪽 팀의 첫번째 인덱스가 됨.
    left = arr[:middle]
    right = arr[middle:]
    return rsp_winner(rsp(left), rsp(right))  # 각 그룹의 승자끼리 가위바위보 시켜서 승자 return


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    cards = list(map(int, input().split()))
    cards = [(cards[i], i + 1) for i in range(n)]  # (가위바위보 정보, 참여자 번호)

    winner = rsp(cards)

    print(f"#{test} {winner[1]}")
