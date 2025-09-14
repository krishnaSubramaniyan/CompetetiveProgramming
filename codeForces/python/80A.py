p = 0
n,m = map(int, input().split())

for i in range(n+1,m+1):
    c = 0
    for j in range(2,i):
        if i%j == 0:
            c += 1
            break

    if c == 0:
        p = i
        break

if p == m:
    print("YES")
else:
    print("NO")
