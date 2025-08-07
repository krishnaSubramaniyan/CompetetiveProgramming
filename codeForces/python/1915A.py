result = []

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] != arr[1]:
        result.append(arr[0])
    else:
        result.append(arr[2])

for i in result:
    print(i)
