result = []

for _ in range(int(input())):
    n = int(input())
    if ((n+1)%3 == 0) or ((n-1)%3 == 0):
        result.append("First")
    else:
        result.append("Second")

for i in result:
    print(i)
