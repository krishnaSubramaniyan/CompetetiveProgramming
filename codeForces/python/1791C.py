for _ in range(int(input())):
    n = int(input())
    bs = input()
    if n == 1:
        print(1)
    else:
        p1 = 0
        p2 = n-1
        for i in range(n//2):
            if bs[p1] != bs[p2]:
                p1 += 1
                p2 -= 1
            else:
                break
        print(len(bs[p1:p2+1]))
