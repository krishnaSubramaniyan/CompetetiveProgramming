for _ in range(int(input())):
    n = int(input())
    arr = tuple(map(int, input().split()))
    if n == 2:
        if arr[0]%2 == arr[1]%2:
            print("YES")
        else:
            print("NO")
    else:
        s1,s2 = 0, sum(arr)
        for i in range(n-1):
            s1 += arr[i]
            s2 -= arr[i]
            if s1%2 == s2%2:
                print("YES")
                s1 = -1
                break
        if s1 == -1:
            continue
        else:
            print("NO")
        
            
            
        
