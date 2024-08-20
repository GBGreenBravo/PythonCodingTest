# 20240819
# 18:00
# 1 / 1


def change_by_man(number):
    now_idx = number - 1  # index + 1로 입력 들어오므로 -1
    while now_idx < n:  # 영역 내 number의 배수만
        switches[now_idx] += 1
        switches[now_idx] %= 2
        now_idx += number


def change_by_woman(number):
    number -= 1  # index + 1로 입력 들어오므로 -1
    left, right = number - 1, number + 1  # 기준 index의 왼쪽 오른쪽 대칭 index들
    while True:
        if left < 0:  # 왼쪽 범위 벗어나면 종료
            break
        if right >= n:  # 오른쪽 범위 벗어나면 종료
            break
        if switches[left] != switches[right]:  # 대칭 안 되면 종료
            break

        left -= 1  # 다음 left, right 설정
        right += 1

    for i in range(left + 1, right):  # 종료 직전의 left, right는 틀렸으므로, left + 1 부터 right - 1 까지.
        switches[i] += 1
        switches[i] %= 2


n = int(input())
switches = list(map(int, input().split()))

people_cnt = int(input())
for _ in range(people_cnt):
    gender, num = map(int, input().split())
    if gender == 1:  # 남자인 경우
        change_by_man(num)
    else:  # 여자인 경우
        change_by_woman(num)

for i in range(n // 20 + 1):  # 20개 단위로 출력
    print(*switches[i * 20:i * 20 + 20])
