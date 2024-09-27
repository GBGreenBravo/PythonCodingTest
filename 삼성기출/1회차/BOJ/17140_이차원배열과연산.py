# 20240830
# 57:00
# 1 / 3

"""
풀이 시간: 57분 (14:33 ~ 15:30)
풀이 시도: 1 / 3


1. 문제 정독 & 풀이 구상 (14:33 - 14:41)
    문제를 읽으며, R연산과 C연산이 근본적으로는 같음을 이해하고,
    하나의 연산 함수만 구현해주고, 반대 연산 전후로 행렬을 반전시켜 주면 된다고 생각했습니다.

    구현의 지시사항들이 체계적으로 정리된 편이 아니었기에,
    메모에 체계를 갖춰 재구성하는 것이 중요했습니다.

    그리고 처음부터 종료조건(r행 c열에 k)를 만족하는 경우에 0을 출력하는지 궁금했기에,
    해당 케이스를 ?로 메모해놓고 구현을 시작했습니다.
    (추후 구현이 모두 끝나고, 테스트케이스 1번에서 바로 확인할 수 있었습니다.)


2. 구현 (14:41 - 14:52)
    C연산을 하기 위해서는 sort_row()함수를 그대로 써주기 위해, 행렬을 반전시켜야 하는데,
    행렬을 (i,i) 라인을 중심으로 반전시켜주는 코드가 바로 기억나지 않았습니다.
    2-3주 전까지만 해도 잘 이용했지만, 떠오르지 않았습니다.
    그래서 일단 행 정렬 함수를 구현해주고 나중에 구현하기로 했습니다. (F11 북마크 표시)


3. 검증 (14:52 - 15:22)
    행 정렬 함수 구현 후, 행/열 반전 구현을 위해
    우선, list(zip(area))로 적어놓고 print()를 통해 확인해봤습니다.
    당연히 문제가 있었기에, 여러번 수정을 해보다가
    모든 코드를 주석 처리하고, 행/열 반전만 확인할 수 있도록 기본 코드들로만 검증하고자 했습니다.

    가장 유력하다고 생각했던, list[row for row in zip(area)]에서도 반환이 이상했으나,
    area가 언패킹 되지 않았음을 그제서야 확인하고, list[row for row in zip(*area)] 로 구현할 수 있었습니다.


4, 런타임 에러 (IndexError) (15:22 - 15:25)
    -1을 출력하기 위한 코드에서도, r과 c의 인덱스 체크를 해줬어야 하는데, 그러지 못했습니다.
    인덱스 에러가 날 코드가 많지 않았기에, 곧바로 실수를 확인할 수 있었습니다.
    문제의 특성상, 행과열이 계속 변하는데 마지막 상태에서도 그럴 수 있음을 간과했습니다..
    인덱스 에러의 경우 정말 치명적인 에러라고 생각하기에,
    앞으로 이런 케이스를 간과하지 않도록, 인덱싱 코드의 행과 열을 좀 더 꼼꼼히 확인해야겠습니다.


4, 틀렸습니다 (15:25 - 15:30)
    잘못된 문제 이해로부터 비롯된 오답이었습니다.
    "100초가 지나도" 에 대해 99초까지만 연산이 가능하다고 이해했으나,
    곰곰이 생각해보면 100초가 지난다는 건, 100초 => 101초의 순간이기 때문에 100초까지 연산해줘야 하는 것이었습니다..

    이 문제의 "while문의 종료"에서만 2개나 실수했기에,
    1) 종료 상태에서의 인덱스 에러 => 인덱싱 범위 체크
    2) 종료 조건에 대한 명확한 검증
    이 요구될 것으로 생각합니다.
"""


def sort_row():
    for r in range(len(area)):
        row = area[r][:100]  # 100개가 넘는 경우 앞 100개까지만. (슬라이싱이라 범위 넘어도 에러 안 남)
        num_dict = dict()    # 숫자별 등장횟수를 저장할 dictionary
        for num in row:    # 현재 행들의 번호에 대해
            if not num:    # 0이면 카운트 안함
                continue
            if num_dict.get(num):  # 기존에 카운트한 적 있는 번호면, +=1
                num_dict[num] += 1
            else:                  # 기존에 카운트 없었던 번호면, =1
                num_dict[num] = 1
        new_row = []       # 정렬되는 수가 들어갈 배열
        for n_num, n_mode in sorted(num_dict.items(), key=lambda x: (x[1], x[0])):  # (빈도수 오름차순, 숫자 오름차순)으로 정렬
            new_row.extend([n_num, n_mode])  # 수-빈도 순서로 추가

        area[r] = new_row  # 정렬된 배열로 갱신

    row_mx_length = len(area[0])
    for row in area:
        row_mx_length = max(row_mx_length, len(row))  # 행 길이 최대값

    for row in area:
        if len(row) < row_mx_length:  # 최대 행 길이보다 짧은 행들은
            row.extend([0] * (row_mx_length - len(row)))  # 0 추가


target_r, target_c, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(3)]

time = 0
while time <= 100:  # 100초까지도 계산해줘야 함.
    len_row = len(area)
    len_col = len(area[0])

    # 앞의 "len_row >= target_r and len_col >= target_c" 조건 꼭 필요함!!
    # 없으면, 뒤 조건에서 인덱싱하는 과정에서 인덱스 에러 뜨기 때문.
    if len_row >= target_r and len_col >= target_c and area[target_r - 1][target_c - 1] == k:
        print(time)
        break

    if len_row >= len_col:                # R연산
        sort_row()  # 행 정렬
    else:  # elif len_row < len_col       # C연산
        area = [list(z_row) for z_row in zip(*area)]  # 행<->열 반전
        sort_row()  # 행 정렬
        area = [list(z_row) for z_row in zip(*area)]  # 행<->열 반전

    time += 1
else:
    print(-1)  # 100초가 지나도 r행 c열이 k가 되지 않으면 -1을 출력
