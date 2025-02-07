input()
counter = [ int(i) for i in input().split(" ") ]
timeCalculation = []
for i in counter:
    sum = 0
    for j in input().split(" "):
        sum += int(j)*5
    sum += (i*15)
    timeCalculation.append(sum)

timeCalculation.sort()
print(timeCalculation[0])
