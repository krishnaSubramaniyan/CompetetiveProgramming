year = int(input())+1

while True:
    if len(set(str(year))) == 4:
        print(year)
        break
    else:
        year += 1
