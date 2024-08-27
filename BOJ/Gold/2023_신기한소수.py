# 20240827
# 19:00
# 1 / 1


def check_prime(number):
    for i in range(3, number, 2):  # 들어오는 수가 짝수는 아니므로, 홀수로만 소수 확인
        if not number % i:
            return False

    return True


n = int(input())

n_idx = 1
now_prime_numbers = [2, 3, 5, 7]  # 1의 자리 소수
while n_idx < n:
    next_prime_numbers = []  # 다음 자리수의 소수 저장될 배열
    for prime_number in now_prime_numbers:
        for i in range(1, 10, 2):
            check_num = prime_number * 10 + i  # '기준을 만족한 현재 소수' 뒤에 1부터 9까지 홀수를 붙여봄. (짝수면 소수 아니므로 pass)
            if check_prime(check_num):
                next_prime_numbers.append(check_num)  # 문제 기준 만족하면 다음 자리수 소수로 추가

    # 다음 반복문을 위한 세팅
    now_prime_numbers = next_prime_numbers
    n_idx += 1

for num in sorted(set(now_prime_numbers)):
    print(num)


# 다른 사람들 풀이와 시간 차이가 꽤 났음.
# 원인: check_prime() 함수의 탐색에서, 제곱근+1까지만 해도 충분하기 때문
"""
from math import sqrt


def check_prime(number):
    for i in range(3, int(sqrt(number)) + 1, 2):  # 제곱근 + 1 까지만 탐색
        if not number % i:
            return False

    return True


n = int(input())

n_idx = 1
now_prime_numbers = [2, 3, 5, 7]
while n_idx < n:
    next_prime_numbers = []
    for prime_number in now_prime_numbers:
        for i in range(1, 10, 2):
            check_num = prime_number * 10 + i
            if check_prime(check_num):
                next_prime_numbers.append(check_num)

    now_prime_numbers = next_prime_numbers
    n_idx += 1

for num in sorted(set(now_prime_numbers)):
    print(num)
"""