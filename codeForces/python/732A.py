n = 1
k,r = map(int, input().split())

while True:
    val = (n*k)%10
    if (val == 0) or (val == r):
        print(n)
        break
    n += 1
