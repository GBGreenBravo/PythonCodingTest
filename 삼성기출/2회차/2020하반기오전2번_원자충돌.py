# 20241003
# 20:08
# 1 / 1

# 20056_마법사상어와파이어볼

"""
풀이 시간: 20분 (16:08 ~ 16:28)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (16:08 - 16:14)


2. 구현 (16:14 - 16:27)
    이전 풀이방식과 거의 차이가 없었습니다.


3. 디버깅 (16:27 - 16:28)
    원자들을 이동시킬 때, 속력만큼이 아닌 1만큼만 이동시켰음을 print디버깅으로 확인하고 수정했습니다.
"""

direction = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

n, m, k = map(int, input().split())
area = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    aa, bb, mm, ss, dd = map(int, input().split())
    area[aa - 1][bb - 1].append((mm, ss, dd))

for _ in range(k):
    new_area = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for mass, speed, d_idx in area[i][j]:
                di, dj = direction[d_idx]
                ni, nj = (i + di * speed) % n, (j + dj * speed) % n

                new_area[ni][nj].append((mass, speed, d_idx))

    for i in range(n):
        for j in range(n):
            len_group = len(new_area[i][j])
            if len_group > 1:
                group_mass = 0
                group_speed = 0
                group_direction = 0
                for mass, speed, d_idx in new_area[i][j]:
                    group_mass += mass
                    group_speed += speed
                    group_direction += d_idx % 2
                group_mass //= 5
                group_speed //= len_group

                new_area[i][j] = []
                if not group_mass:
                    continue
                start_d_idx = int(group_direction not in (0, len_group))
                for new_d_idx in range(start_d_idx, 8, 2):
                    new_area[i][j].append((group_mass, group_speed, new_d_idx))

    area = new_area

answer = 0
for i in range(n):
    for j in range(n):
        answer += sum([ij[0] for ij in area[i][j]])
print(answer)
