n = int(input())
x = 0

for _ in range(n):
    operation = input()
    if operation == "X++" or operation == "++X":
        x += 1
    else:
        x -= 1

print(x)
