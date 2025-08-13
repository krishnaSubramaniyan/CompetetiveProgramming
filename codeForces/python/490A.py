programmer,math,PE = [],[],[]

n = int(input())
stud = input().split()
stud.insert(0,0)
for i in range(n+1):
    match stud[i]:
        case '1':
            programmer.append(i)
        case '2':
            math.append(i)
        case '3':
            PE.append(i)

count = min(len(programmer), len(math), len(PE))

print(count)
if count > 0:
    for i in range(count):
        print(programmer[i],math[i],PE[i])
