n = int(input())
groups = 0
previous_magnet = ''
for i in range(n):
    magnet = input()
    if i == 0:
        groups += 1
    else:
        if previous_magnet != magnet:
            groups += 1
    previous_magnet = magnet

print(groups)
