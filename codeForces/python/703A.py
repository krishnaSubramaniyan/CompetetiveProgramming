m,c = 0,0
for _ in range(int(input())):
    arr = tuple(map(int, input().split()))

    if arr[0] > arr[1]:
        m += 1
    elif arr[1] > arr[0]:
        c += 1

if m > c:
    print("Mishka")
elif c > m:
    print("Chris")
else:
    print("Friendship is magic!^^")
