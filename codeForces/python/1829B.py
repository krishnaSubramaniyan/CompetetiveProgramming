for _ in range(int(input())):
    n = int(input())
    b = input().split()
    space, temp = 0,0

    for i in range(n):
        if b[i] == '0':
            temp += 1
        if b[i] == '1' or i == n-1:
            if temp > space:
                space = temp
            temp = 0

    print(space)
    
