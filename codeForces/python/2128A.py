coins = []

for i in range(int(input())):
    coin_count = 0
    n,c = map(int, input().split())
    l1 = map(int, input().split())
    l2 = []
    for i in l1:
        if i <= c:
            l2.append(i)
    coin_count = n - len(l2)
    
    while len(l2) != 0:
        select = max(l2)
        l2.pop(l2.index(select))
        temp = []
        for i in l2:
            i *= 2
            if i > c:
                coin_count += 1
            else:
                temp.append(i)
        l2 = temp
        
    coins.append(coin_count)

for i in coins:
    print(i)
