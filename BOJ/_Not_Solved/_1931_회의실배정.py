import sys
sys.stdin = open("../input.txt", "r")

n = int(input())
start_time = 2**31 - 1
meetings = []
for _ in range(n):
    meetings.append(list(map(int, input().split())))
    start_time = min(start_time, meetings[-1][0])

for i in range(n):
    meetings[i][0] -= start_time
    meetings[i][1] -= start_time

start_times = [list() for _ in range(max([i[1] for i in meetings]) + 1)]
for i in range(n):
    start_times[meetings[i][1]].append(meetings[i][0])

mx_meetings = [0] * (max([i[1] for i in meetings]) + 1)
mx_meetings[0] = start_times[0].count(0)
for i in range(1, len(mx_meetings)):
    mx = 0
    for start in start_times[i]:
        now = mx_meetings[start] + sum([1 for k in start_times[i] if k >= start])
        mx = max(mx, now)
    mx_meetings[i] = max(mx, mx_meetings[i - 1])

print(max(mx_meetings))
print(mx_meetings)
# 53:39
