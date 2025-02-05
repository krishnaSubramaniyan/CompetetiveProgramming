day = input().split()

if(day[2] == "week"):
    trigger = int(day[0])
    count = 0
    if(trigger > 4):
        trigger -= 4
    else:
        trigger += 3
    for i in range(1,367):
        if(i == trigger):
            count += 1
            trigger += 7
            print(count)
    else:
        if(day[0] == '31'):
            print(7)
        elif(day[0] == '30'):
            print(11)
        else:
            print(12)
