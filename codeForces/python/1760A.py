result = []

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    result.append(arr[1])

for i in result:
    print(i)
