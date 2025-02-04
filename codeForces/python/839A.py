day,target = [int(i) for i in input().split(" ")]
candyBox = [int(i) for i in  input().split(" ")]
candies = 0
days = 0

for i in range(day):
    candies += candyBox[i];
    if(target < 1):
        break
    elif(target > 0 and candies >= 8):
        target -= 8
        candies -= 8
        days += 1
    elif(candies < 8):
        target -= candies
        candies = 0
        days += 1

if(target>0):
    print(-1)
else:
    print(days)
