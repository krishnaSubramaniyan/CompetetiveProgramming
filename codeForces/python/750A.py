solved_count = 0
n, remaining_time = map(int, input().split())
remaining_time = 240 - remaining_time

for i in range(1,n+1):
    taking_time = i*5
    if remaining_time >= taking_time:
        remaining_time -= taking_time
        solved_count += 1
    else:
        break

print(solved_count)
