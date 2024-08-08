# 20240808
# 43:51
# 1 / 2


def check_diagonal(arr):  # 가장 최근에 추가된(배열의 마지막 행에 추가된) queen의 대각선에 다른 queen이 존재하는지 판단하는 함수
    arr_len = len(arr)

    last = arr[-1]  # 가장 최근에 추가된(배열의 마지막 행에 추가된) queen
    for i in range(arr_len - 1):
        if arr_len - 1 - i == abs(last - arr[i]):  # 앞의 배열에 대각선에 존재하는 queen이 있다면
            return True

    return False


def one_for_row_and_column(queen_cnt, arr, visited, first_row_is_middle):  # 현재배열에 저장된 queen 수, 현재배열, 열 중복을 방지하기 위한 방문배열, 첫번째 행의 정가운데 index에 퀸이 있는지 유무
    if arr and check_diagonal(arr):  # 현재 배열이 존재하고 가장 최근에 추가된(배열의 마지막 행에 추가된) queen의 대각선에 다른 queen이 존재한다면
        return

    if queen_cnt == n:  # queen을 다 채웠다면
        global answer
        answer += 1 if first_row_is_middle else 2  # 첫번째 행의 정가운데에 queen이 있다면 1 추가 / 아니라면(가운데 전 index만 순회하므로 같은 모양의 좌우반전 1개 더 있음) 2 추가
        return

    for i in range(n):
        if not arr:  # 첫번째 행의 차례라면
            if i < n // 2:  # 정가운데 전의 index만 탐색 (좌우반전만 하면 반대편 index로 시작하는 모양도 탐지할 수 있기 때문)
                visited[i] = True
                one_for_row_and_column(queen_cnt + 1, arr + [i], visited, False)
                visited[i] = False
            elif n % 2 == 1 and i == n // 2:  # n이 홀수고 정가운데의 index로 시작한다면, 좌우반전해도 이미 count돼 있기에 따로 취급.
                visited[i] = True
                one_for_row_and_column(queen_cnt + 1, arr + [i], visited, True)
                visited[i] = False
        elif not visited[i]:  # 첫번째 행 아니고, 이전 행에서 사용하지 않은 열이라면 (row, column 겹치지 않도록)
            visited[i] = True
            one_for_row_and_column(queen_cnt + 1, arr + [i], visited, first_row_is_middle)
            visited[i] = False


n = int(input())
answer = 0  # 경우의 수를 카운트
one_for_row_and_column(0, [], [False] * n, None)
print(answer)


# arr과 visited를 인자로 담기보다, 전역변수로 관리하는 게 메모리 상이나 속도 상으로 더 좋음
"""
def check_diagonal():  # 가장 최근에 추가된(배열의 마지막 행에 추가된) queen의 대각선에 다른 queen이 존재하는지 판단하는 함수
    arr_len = len(arr)

    last = arr[-1]  # 가장 최근에 추가된(배열의 마지막 행에 추가된) queen
    for i in range(arr_len - 1):
        if arr_len - 1 - i == abs(last - arr[i]):  # 앞의 배열에 대각선에 존재하는 queen이 있다면
            return True

    return False


def one_for_row_and_column(queen_cnt, first_row_is_middle):  # 현재배열에 저장된 queen 수, 현재배열, 열 중복을 방지하기 위한 방문배열, 첫번째 행의 정가운데 index에 퀸이 있는지 유무
    if arr and check_diagonal():  # 현재 배열이 존재하고 가장 최근에 추가된(배열의 마지막 행에 추가된) queen의 대각선에 다른 queen이 존재한다면
        return

    if queen_cnt == n:  # queen을 다 채웠다면
        global answer
        answer += 1 if first_row_is_middle else 2  # 첫번째 행의 정가운데에 queen이 있다면 1 추가 / 아니라면(가운데 전 index만 순회하므로 같은 모양의 좌우반전 1개 더 있음) 2 추가
        return

    for i in range(n):
        if not arr:  # 첫번째 행의 차례라면
            if i < n // 2:  # 정가운데 전의 index만 탐색 (좌우반전만 하면 반대편 index로 시작하는 모양도 탐지할 수 있기 때문)
                visited[i] = True
                arr.append(i)
                one_for_row_and_column(queen_cnt + 1, False)
                arr.pop()
                visited[i] = False
            elif n % 2 == 1 and i == n // 2:  # n이 홀수고 정가운데의 index로 시작한다면, 좌우반전해도 이미 count돼 있기에 따로 취급.
                visited[i] = True
                arr.append(i)
                one_for_row_and_column(queen_cnt + 1, True)
                arr.pop()
                visited[i] = False
        elif not visited[i]:  # 첫번째 행 아니고, 이전 행에서 사용하지 않은 열이라면 (row, column 겹치지 않도록)
            visited[i] = True
            arr.append(i)
            one_for_row_and_column(queen_cnt + 1, first_row_is_middle)
            arr.pop()
            visited[i] = False


n = int(input())
answer = 0  # 경우의 수를 카운트
arr = []  # 현재배열
visited = [False] * n  # 열 중복을 방지하기 위한 방문배열
one_for_row_and_column(0, None)
print(answer)
"""