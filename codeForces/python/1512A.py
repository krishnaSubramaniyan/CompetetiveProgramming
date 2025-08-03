result = []

for _ in range(int(input())):
    n = int(input())
    arr = tuple(map(int, input().split()))

    repeat = None
    if arr[0] == arr[1]:
        repeat = 0
    elif arr[1] == arr[2]:
        repeat = 1
    elif arr[0] == arr[2]:
        repeat = 2

    for i in range(n):
        if arr[repeat] != arr[i]:
            result.append(i+1)

for i in result:
    print(i)
