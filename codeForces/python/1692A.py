result = []
for t in range(int(input())):
    result.append(0)
    distance = tuple(map(int, input().split()))
    for i in range(1,4):
        if distance[i] > distance[0] :
            result[t] += 1

for i in result:
    print(i)
