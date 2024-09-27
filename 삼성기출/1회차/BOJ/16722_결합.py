# 20240822
# 21:00
# 1 / 1

"""
풀이 시간: 21분 (14:30 ~ 14:51)
풀이 시도: 1 / 1


1. 문제 정독 (14:30 - 14:35)
    (아래는 문제를 읽는 당시, 메모한 사항을 모두 옮겨적은 것입니다.)
    - 구분
        모양: ㅇ ㅁ ㅅ
        색: 노 빨 파
        배경색: 회 흰 검
    - 27장 중 9장
    - command - 합 - 이전X "+1"
                   - 이전O "-1"
              - 결 - 합 더이상 X and 결로 점수 안 얻었다면 "+3"
                   - 합 여전히 0 "-1"
    - 모든 조합(comb(9, 3))
      -> 합 조합 저장
      -> 플레이어 게임 실행
         (합 visited / 결 점수 여부)


2. 풀이 구상 (14:30 - 14:36)
    9개에서 3개의 조합을 선택하는 것으로, 시간이 오래 걸리지 않기에,
    1) 모든 3개의 조합을 점검하고, 합이 되는 조합을 저장해도 된다고 생각했습니다.
    2) 플레이어의 게임 기록에 대한 점수 연산은 위의 과정 후에 해야 할 것이라고 설계했습니다.

    1) 백트래킹으로 3장의 카드를 선택하고,
       합 여부 판단 함수를 통해, 별도의 리스트에 합이 되는 정보를 저장하면 됩니다.

    2) 유의할 점들은, '기존에 외쳐진 합인지'와 '결로 이미 점수를 얻었는지'입니다.
        각각, '합을 이루는 조합에 대한 방문배열'과 'True/False flag로 체크'
        로 다뤄주면 됨을 인지했습니다.


3. 구현 (14:36 - 14:49)
    구현을 하며, 현재 생각하고 있는 부분을 작성하기 위해,
    불가피하게 if/else에 대한 처리 중 한 부분만을 하고 다음 줄의 코드로 넘어가는 경우가 종종 있습니다.

    저는 그러한 경우에 "# ?"와 같은 주석이나 pass와 같은 코드를 활용하여,
    나중에 꼭 처리해줘야 하는 부분임을 명시적으로 표시하는 편입니다.


4. 검증 (14:49 - 14:51)
    구현을 마치고, 테스트케이스에 대한 실행을 했을 때, 항상 감점만 되어 -9가 출력되었습니다.
    해당 출력이, 문자열로 받은 카드 번호들을 숫자형으로 변환해주지 않음을 바로 발견하고, 수정했습니다.
"""


# now_pictures_arr에 있는 3개의 카드index들로부터, 해당 카드가 합을 이루는지, 이룬다면 그 배열을 저장하는 함수
def check_hap():
    shape = set()  # 모양
    color = set()  # 색
    back = set()  # 배경색
    for i in now_pictures_arr:  # 현재 담겨있는 3개의 카드 인덱스에 대해
        s, c, b = pictures[i]
        shape.add(s)
        color.add(c)
        back.add(b)

    # 각 set의 길이가 무조건 1,2,3 셋 중 하나일 텐데,
    # 하나라도 2의 길이를 가지면 합이 아님.
    if len(shape) != 2 and len(color) != 2 and len(back) != 2:
        hap_indexes.append(tuple(now_pictures_arr))  # 합인 경우에, 해당 구성을 저장


# 9개의 카드 중에 3개를 선택(comb(9,3))하고, 위 함수를 호출하는, DFS/백트래킹 함수
def get_three_pictures(cnt, start_idx):
    # 종료 조건: 3개의 카드를 선택했을 때
    if cnt == 3:
        check_hap()
        return

    # 현재 배열 마지막에 담긴 카드번호 다음으로, 추가할 수 있는 다음 카드번호
    for i in range(start_idx, 9):
        now_pictures_arr.append(i)
        get_three_pictures(cnt + 1, i + 1)
        now_pictures_arr.pop()


pictures = [tuple(map(str, input().split())) for _ in range(9)]

hap_indexes = []  # 합을 구성하는 카드들의 index가 담길 리스트

now_pictures_arr = []  # DFS를 하며, 현재 구성되는 카드들의 index가 담길 리스트
get_three_pictures(0, 0)


# 위의 코드까지는 9장을 입력 받고, 합이 구성되는 3장의 index를 튜플로 구성하여 리스트에 담아준 과정입니다.
# 아래부터는 플레이어의 게임 기록에 대한, 점수를 계산해주는 코드입니다.


n = int(input())
commands = [tuple(map(str, input().split())) for _ in range(n)]

# 합을 구성하는 조합별로, '기존에 외쳐진 합인지'를 판단해줄 방문배열
hap_indexes_visited = [0] * len(hap_indexes)

total_score = 0  # 최종으로 출력될 총점수
gyeol_score_added = False  # 결로 점수가 추가됐는지를 체크하는 flag
for command in commands:
    if command[0] == 'G':  # 결 커맨드
        if sum(hap_indexes_visited) == len(hap_indexes) and not gyeol_score_added:
            gyeol_score_added = True
            total_score += 3
        else:
            total_score -= 1
    else:  # 합 커맨드
        hap_object = tuple(sorted([int(i) - 1 for i in command[1:]]))
        if hap_object in hap_indexes and not hap_indexes_visited[hap_indexes.index(hap_object)]:
            total_score += 1
            hap_indexes_visited[hap_indexes.index(hap_object)] = 1
        else:
            total_score -= 1
print(total_score)
