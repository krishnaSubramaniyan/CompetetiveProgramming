result = []
for t in range(int(input())):
    result.append("NO")
    num = [int(i) for i in input()]
    if sum(num[0:3]) == sum(num[3:6]):
        result[t] = "YES"

for i in result:
    print(i)
