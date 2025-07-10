n = int(input())
a = input().split(" ")
p = [int(i) for i in a]
r = [-1 for i in range(n)]

for i in p:
    r[(i-1)] = p.index(i)+1

print(*r)
