# 20240806
# 07:00
# 1 / 1


def merge_powers(index, cnt, sm):  # 현재의 함수에서 추가 유무 판별할 powers의 인덱스 / 이전까지 합쳐온 powers 수 / 합쳐온 총합
    global answer_cnt

    if cnt > m:  # 조기 종료조건: 이전까지 합쳐온 power 수가 이미 m을 초과할 때
        return

    if index == n:  # 종료조건: 이전의 함수에서 마지막 인덱스까지 탐색한 경우
        if cnt == m and sm == k:  # 개수와 총합을 만족한다면 answer_cnt += 1
            answer_cnt += 1
        return

    merge_powers(index + 1, cnt + 1, sm + powers[index])  # 지금의 index의 power 추가하는 경우
    merge_powers(index + 1, cnt, sm)  # 지금의 index의 power 추가하지 않는 경우


t = int(input())
for test in range(1, t + 1):
    n, m, k = map(int, input().split())
    powers = list(map(int, input().split()))

    answer_cnt = 0
    merge_powers(0, 0, 0)
    print(f"#{test} {answer_cnt}")
