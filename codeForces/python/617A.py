length = int(input())
steps = 0

while True:
    length -= 5
    steps  += 1
    if length < 1:
        break

print(steps)
