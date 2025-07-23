cord = [int(i) for i in input().split()]
cord.sort()
print((cord[1]-cord[0]) + (cord[2]-cord[1]))
