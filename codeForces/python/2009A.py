result = []

for _ in range(int(input())):
    a,b = map(int, input().split())
    result.append((b-a))

for i in result:
    print(i)
