result = []

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    if (arr[1]+arr[2]) >= 10:
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)
