for _ in range(int(input())):
    i,a = 1,0
    n = input()
    while(i != int(n[0])):
        a += 10
        i += 1
    n = len(n)
    a += int(n * (n+1)/2)
    print(a)
