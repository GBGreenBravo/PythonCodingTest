# 20240811
# 1:30:24
# 1 / 4

# 알파벳 26개에서 기본 5개를 뺀 것중 k-5개의 조합을 적용해보면 되는 문제. (352716)
# 여기서 50개의 word에 대해 구성 가능 여부를 검사해주는 시간복잡도를 줄이는 것이 포인트였음.

"""
1. 문제 분석
- DFS, 백트래킹
- 단어별 {'a', 'c', 'i', 'n', 't'} 말고 추가로 요구되는 알파벳을, K - 5개 내의 제한된 학습 알파벳으로 포함시킬 수 있는지.

2. 설계
- 기본 알파벳인 {'a', 'c', 'i', 'n', 't'} 말고 추가로 요구하는 알파벳만을 words에 저장한다.
- dfs()로 words의 인덱스를 순회하며 해당 word에서 요구하는 알파벳을 set에 합쳐나간다.
- 합친 조합에서 남은 알파벳 부족하거나 범위 밖이면, return (조기 종료)
- 현재 dfs()에서 알파벳 조합 길이가 limit이 됐다면 return (종료)
- 최대치로 했을 떼, 시간 1초 이상 걸리면 별도의 가지치기 필요.

3. 구현
- 조합된 알파벳의 word 구성 가능성 여부 => 비트연산자 활용
- b와 d를 활용한 경우, 1100000... 과 같은 이진수로 변환하고자 함.
- words의 word를 다 이진수로 변환해서 저장한 다음,
- dfs()에서 조합된 알파벳도 이진수로 변환하고,
- word이진수 & 조합된알파벳이진수 == word이진수면, word가 조합된 알파벳으로 구성 가능한지 여부 판단할 수 있음.

4. 검증
- n, k를 50 26 최대치로 했을 때, 시간 오래 걸림. 별도의 가지치기 필요.
- 처음에 틀렸던 풀이는, 중복검사에서 틀리기도 했고 50개의 word에서 알파벳을 뽑아서 시간이 더 걸리는 풀이였음.
- 수정한 풀이는, 21개의 알파벳에서 조합해서 시간복잡도 줄임.
- 조합된 알파벳의 word 구성 가능성 여부는 비트연산자 활용함.
"""

n, k = map(int, input().split())
now_set = {'a', 'c', 'i', 'n', 't'}  # anta, tica의 prefix, suffix에 쓰이는 기본 알파벳 5개
alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}  # 모든 알파벳
candidates = list(alphabets - now_set)  # 기본 알파벳 뺀, 조합에서 사용 가능한 알파벳들
limit = k - 5  # 기본 알파벳 5개를 뺀, 알파벳 조합의 길이


def change_arr_to_binary(arr):  # 알파벳 배열을 받아, 비트연산자를 활용한 이진수를 반환하는 함수
    result = 0
    for alphabet in candidates:
        if alphabet in arr:
            result += 1
        result = result << 1
    return result


def dfs(cnt, start_index):  # 21 C limit 의 조합에 대한 DFS
    if cnt == limit:  # 조합의 길이가 limit으로 완성되면
        global mx
        alpha_arr_binary = change_arr_to_binary(alpha_arr)  # 완성된 알파벳 조합을 이진수로 변환하고
        mx = max(mx, sum([1 for word in words if word & alpha_arr_binary == word]))  # 해당 이진수&word이진수 == word이진수인 (alpha_arr로 구성 가능한) word의 개수의 최대값 갱신
        return

    if start_index == 21 or 21 - start_index < limit - cnt:  # 조합 구성 범위/개수 밖이면 return
        return

    for i in range(start_index, 21):  # 21; 26개 알파벳에서 기본알파벳 5개를 뺀 len()
        alpha_arr.append(candidates[i])
        dfs(cnt + 1, i + 1)
        alpha_arr.pop()


words = [change_arr_to_binary(set(str(input())) - now_set) for _ in range(n)]  # '해당 word에 사용되는 알파벳에서 기본알파벳을 뺀 조합을 이진수로 변환한 값'들의 리스트

if limit < 0:  # 기본알파벳 5개도 사용 못하면 0 출력
    print(0)
else:  # 5개 이상의 알파벳을 쓸 수 있을 때
    mx = 0
    alpha_arr = []  # 조합에서 구성되는 알파벳을 저장할 리스트
    dfs(0, 0)
    print(mx)


# 아래는 틀린 풀이. 중복검사에서 빠진 부분 있었음. 예시 테스트케이스는 맨 아래.
"""
def dfs(start_index, dfs_set):
    if len(dfs_set) > limit:
        return

    global mx
    mx = max(mx, sum([1 for i in words if not i.difference(dfs_set)]))

    if start_index == n:
        return

    for i in range(start_index, n):
        dfs_set_union = dfs_set.union(words[i])
        for already in already_checked:
            if i >= already[0] and not dfs_set_union.difference(set(already[1])):
                break
        else:
            dfs(i + 1, dfs_set_union)
            already_checked.add((i, tuple(dfs_set_union)))


n, k = map(int, input().split())
now_set = {'a', 'c', 'i', 'n', 't'}
limit = k - 5

words = [set(str(input())) - now_set for _ in range(n)]

if limit <= 0:
    print(0)
else:
    mx = 0
    already_checked = set()
    dfs(0, set())
    print(mx)
"""
"""
6 7
antarmtica
antartica
antaktica
antarktica
antarkktica
antakktica
"""