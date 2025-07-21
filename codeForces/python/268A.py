conflit = 0
teams = int(input())
uniform = [tuple(input().split()) for _ in range(teams)]

for i in range(teams):
    for j in range(teams):
        if i == j:
            continue
        if uniform[i][0] == uniform[j][1]:
            conflit += 1

print(conflit)
