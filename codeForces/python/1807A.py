result = []

for t in range(int(input())):
    result.append('-')
    num = tuple(map(int, input().split()))
    if (num[0]+num[1]) == num[2]:
        result[t] = '+'

for i in result:
    print(i)
