n = int(input())
temp = n - 4

while True:
    c = 0
    for i in range(2,temp):
        if temp%i == 0:
            break
    else:
        temp -= 2
        continue
    break

print(n-temp, temp)
