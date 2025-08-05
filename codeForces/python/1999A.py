result = []

for _ in range(int(input())):
    n = int(input())
    result.append((n//10)+(n%10))

for i in result:
    print(i)
