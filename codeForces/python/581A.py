a,b = map(int, input().split())

if a > b:
    a -= b
    print(f'{b} {a//2}')
else:
    b -= a
    print(f'{a} {b//2}')
