for _ in range(int(input())):
    a,b,c,d = map(int, input().split())

    t = False
    for i,j in (a,b),(abs(a-c),abs(b-d)):
        if i > j:
            i = i - (j*2)
            if i > 2:
                t = True
                print("NO")
                break
        else:
            j =  j - (i*2)
            if j > 2:
                t = True
                print("NO")
                break
    if t==False:
        print("YES")
