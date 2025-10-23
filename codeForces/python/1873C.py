def score(mainString,line):
    for s in [mainString[:5],mainString[-1:-6:-1]]:
        match(line):
            case 0:
                count[0] += s.count('X')
            case 1:
                for i in range(5):
                    if s[i] == 'X':
                        if i != 0:
                            count[1] += 1
                        else:
                            count[0] += 1
            case 2:
                for i in range(5):
                    if s[i] == 'X':
                        match(i):
                            case 0:
                                count[0] += 1
                            case 1:
                                count[1] += 1
                            case _:
                                count[2] += 1
            case 3:
                for i in range(5):
                    if s[i] == 'X':
                        if i == 3 or i == 4:
                            count[3] += 1
                        else:
                            count[i] += 1
            case 4:
                for i in range(5):
                    if s[i] == 'X':
                        count[i] += 1


for _ in range(int(input())):
    count = [0,0,0,0,0]
    line = 10
    for i in range(10):
        line -= 1
        string = input()
        if 'X' in string:
            if i > 4:
                score(string,line)
            else:
                score(string,i)

    print(count[0]+(count[1]*2)+(count[2]*3)+(count[3]*4)+(count[4]*5))
