limak, bob = map(int, input().split(" "))
year = 0

while True:
    year += 1
    limak *= 3
    bob *= 2
    if limak > bob :
        break

print(year)
