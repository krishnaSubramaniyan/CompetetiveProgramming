for _ in range(int(input())):
    num = tuple(map(int, input().split()))
    if num[0] < num[1]:
        if num[1] < num[2]:
            print("STAIR")
            continue
        elif num[1] > num[2]:
            print("PEAK")
            continue
    print("NONE")
