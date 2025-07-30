result = []
for _ in range(int(input())):
    a,b = map(int, input().split())
    diff = abs(a-b)
    if diff == 0:
        result.append(0)
    elif diff > 9:
        a = diff%10
        b = diff//10
        if a > 0:
            b += 1
        result.append(b)
    else:
        result.append(1)

for i in result:
    print(i)
