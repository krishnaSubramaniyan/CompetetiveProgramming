for _ in range(int(input())):
    input()
    arr = tuple(map(int, input().split()))
    print(max(arr)-min(arr))
