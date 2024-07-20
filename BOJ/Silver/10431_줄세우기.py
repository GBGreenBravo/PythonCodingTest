# 20240720

p = int(input())

result = []

for _ in range(p):
    count = 0

    case_number, *heights = map(int, input().split(" "))

    students = list(heights)

    line = [students.pop(0)]
    max_height = line[0]
    for student in students:
        height_diff = 999999
        diff_index = None
        for li in line:
            li_diff = li - student
            if 0 < li_diff and li_diff < height_diff:
                height_diff = li_diff
                diff_index = line.index(li)

        if height_diff == 999999:
            line.append(student)
            continue
        else:
            count += len(line) - diff_index
            line.insert(diff_index, student)

    result.append((case_number, count))

for i in result:
    print(i[0], i[1])
