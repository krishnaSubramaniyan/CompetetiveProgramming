for _ in range(int(input())):
    n,k = map(int, input().split())
    if k > 1:
        input()
        print("YES")
    else:
        arr = tuple(map(int, input().split()))
        for i in range(n-1):
            if arr[i] <= arr[i+1]:
                continue
            else:
                print("NO")
                k = 0
                break
        if k != 0:
            print("YES")
