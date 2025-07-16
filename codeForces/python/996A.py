notes = 0
doller = int(input())

for i in (100, 20, 10, 5, 1):
    if doller == 0:
        break
    if doller >= i:
        notes += doller//i
        doller %= i

print(notes)
