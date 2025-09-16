from math import floor

for _ in range(int(input())):
    x,y,n = map(int, input().split())
    print(x*floor((n-y)/x)+y)
