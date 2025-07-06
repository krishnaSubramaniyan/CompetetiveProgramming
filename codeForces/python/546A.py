# using sum of n numbers formula n(n+1)/2

k,n,w = map(int, input().split(" "))

rate = int((w * (w+1)/2) * k)

borrow =  rate - n

if borrow < 0:
    print(0)
else:
    print(borrow)
