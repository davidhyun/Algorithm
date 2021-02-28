N = int(input())
time_arr = list(map(int, input().split()))

_sorted = sorted(time_arr)
cumulative_time = 0
result = []
for time in _sorted:
    cumulative_time += time
    result.append(cumulative_time)

print(sum(result))
