for _ in range(int(input())):
    h,m = map(int, input().split())
    t = 60 - m
    if h != 23:
        t += (23-h) * 60
    print(t)
