# 20240722
# 04:46

n = int(input())
numbers = list(map(int, input().split()))

sorted_numbers_set = sorted(list(set(numbers)))
sorted_numbers_dict = {}
for i in range(len(sorted_numbers_set)):
    sorted_numbers_dict[sorted_numbers_set[i]] = i

for number in numbers:
    print(sorted_numbers_dict[number], end=" ")


# zip()을 활용하면 dict 만드는 코드 단축 가능.
'''
n = int(input())
numbers = list(map(int, input().split()))

sorted_numbers_set = sorted(list(set(numbers)))
sorted_numbers_dict = dict(zip(sorted_numbers_set, range(len(sorted_numbers_set))))

for number in numbers:
    print(sorted_numbers_dict[number], end=" ")
'''


# 추가로 enumerate() 활용하면 아래와 같이.
# 그리고 sorted_numbers_set 선언 시, sorted()는 리스트를 반환하므로, 안에 list() 씌울 필요 없음.
'''
n = int(input())
numbers = list(map(int, input().split()))

sorted_numbers_set = sorted(set(numbers))
sorted_numbers_dict = {x[1]: x[0] for x in enumerate(sorted_numbers_set)}

for number in numbers:
    print(sorted_numbers_dict[number], end=" ")
'''
