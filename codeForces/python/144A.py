n = int(input())-1
soldiers = list(map(int, input().split()))
moves = 0

# swap max value
max_value = max(soldiers)
max_index = soldiers.index(max_value)
if max_index != 0:
    soldiers.pop(max_index)
    soldiers.insert(0,max_value)
    moves += max_index

# swap min value
min_value = min(soldiers)
min_index = None
for i in range(n,-1,-1):
    if soldiers[i] == min_value:
        min_index = i
        break

if min_index != n:
    moves += n - min_index

print(moves)
