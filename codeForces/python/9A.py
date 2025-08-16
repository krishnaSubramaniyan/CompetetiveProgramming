M = max(map(int, input().split()))
m = 7-M

if m == 5:
    print("5/6")
elif m == 4:
    print("2/3")
else:
    print(f'1/{6//m}')
