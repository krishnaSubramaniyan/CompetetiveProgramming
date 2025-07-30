result = []
for _ in range(int(input())):
    p = 0
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    for i in range(1,n):
        if (a[p] == a[p+1]) or (a[p]+1 == a[p+1]):
            a.pop(0)
        else:
            p += 1
            if p > 1:
                break

    if len(a) == 1:
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)
