for _ in range(int(input())):
    n = int(input())
    s = sum(map(int, input().split()))

    if n == s:
        print(0)
    elif s > n:
        print(s-n)
    else:
        print(1)
