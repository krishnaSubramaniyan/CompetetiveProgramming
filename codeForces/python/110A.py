n = input()
numbers_count = 0

for i in n:
    if (i=='4') or (i=='7'):
        numbers_count += 1

if (numbers_count==4) or (numbers_count==7):
    print("YES")
else:
    print("NO")
