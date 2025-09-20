for _ in range(int(input())):
    x,y = map(int, input().split())
    if x < y:
        print(2)
    elif x == y:
        print(-1)
    else:
        if (y > 1) and ((x-1) != y):
            print(3)
        else:
            print(-1)        
