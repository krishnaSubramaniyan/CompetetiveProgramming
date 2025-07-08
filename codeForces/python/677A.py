_,h = map(int, input().split(" "))
friends = map(int, input().split(" "))

width = 0
for i in friends:
    if i > h:
        width += 2
    else:
        width += 1

print(width)
