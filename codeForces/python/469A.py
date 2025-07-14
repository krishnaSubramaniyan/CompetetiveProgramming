level = int(input())
little_x = set(input().split()[1:])
little_x.update(input().split()[1:])

if '0' in little_x:
    little_x.remove('0')

if len(little_x) == level:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
