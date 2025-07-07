input()
anton_win, danik_win = 0,0

for i in input():
    if i == 'A':
        anton_win += 1
    else:
        danik_win += 1

if anton_win > danik_win:
    print("Anton")
elif danik_win > anton_win:
    print("Danik")
else:
    print("Friendship")
