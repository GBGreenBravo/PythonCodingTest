# 20240820
# 13:00
# 1 / 1

english = 'qwertyuiopasdfghjklzxcvbnm'  # 딕셔너리에 저장할 알파벳들 순서대로
indexes = ((True, 0, 0), (True, 0, 1), (True, 0, 2), (True, 0, 3), (True, 0, 4), (False, 0, 5), (False, 0, 6), (False, 0, 7), (False, 0, 8), (False, 0, 9),
           (True, 1, 0), (True, 1, 1), (True, 1, 2), (True, 1, 3), (True, 1, 4), (False, 1, 5), (False, 1, 6), (False, 1, 7), (False, 1, 8),
           (True, 2, 0), (True, 2, 1), (True, 2, 2), (True, 2, 3), (False, 2, 4), (False, 2, 5), (False, 2, 6))  # 한글자음여부, 거리계산할 좌표

eng_to_kor = dict(zip(english, indexes))  # english를 key로 가지고, indexes를 value로 가지는 딕셔너리

l, r = map(str, input().split())
l, r = eng_to_kor[l][1:], eng_to_kor[r][1:]  # 시작할 때의 왼손/오른손 좌표 저장

time = 0
words = str(input())
for alpha in words:
    korean_flag, ny, nx = eng_to_kor[alpha]  # 다음 단어의 (한글 자음 여부, *좌표) 가져오기
    if korean_flag:  # 한글 자음이면 왼손
        time += abs(ny - l[0]) + abs(nx - l[1])  # 거리 계산 및 반영
        l = (ny, nx)  # 왼손 좌표 변경
    else:  # 한글 모음이면 오른손
        time += abs(ny - r[0]) + abs(nx - r[1])  # 거리 계산 및 반영
        r = (ny, nx)  # 오른손 좌표 변경
    time += 1  # 키보드 누르는 시간 1

print(time)
