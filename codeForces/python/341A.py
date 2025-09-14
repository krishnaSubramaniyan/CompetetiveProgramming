burned_calories = 0
c = tuple(map(int, input().split()))

for i in input():
    burned_calories += c[int(i)-1]

print(burned_calories)
