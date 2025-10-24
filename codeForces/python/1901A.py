for _ in range(int(input())):
    n,x = map(int, input().split())
    s = tuple(map(int, input().split()))
    t = s[0]
    for i in range(n-1):
        temp = s[i+1] - s[i]
        if temp > t:
            t = temp
    temp = (x - s[-1])*2
    if temp > t:
        t = temp

    print(t)
