count = int(input())
numbers = [int(input()) for i in range(count)]

for i in range(count):
    num = numbers[i]
    temp = 0
    cal = []
    for j in (10000, 1000, 100, 10, 1):
        if num >= j:
            temp = num
            num %= j
            cal.append(temp-num)
    print(len(cal))
    print(*cal)
