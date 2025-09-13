num = []
for _ in range(int(input())):
    num.append(int(input()))

m = max(num)
odd = range(1,m+1,2)
even = range(2,m+1,2)

for i in num:
    if i%4 != 0:
        print("NO")
    else:
        print("YES")
        m = i//2
        for j in range(m):
            print(even[j],end=" ")
        for k in range(m-1):
            print(odd[k],end=" ")
        print(odd[m-1]+even[(m-1)//2])
