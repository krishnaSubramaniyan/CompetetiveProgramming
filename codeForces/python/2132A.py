for _ in range(int(input())):
    input() #length
    str1 = list(input())
    n = int(input())
    str2 = input()
    str3 = input()
    for i in range(n):
        if str3[i] == 'D':
            str1.append(str2[i])
        else:
            str1.insert(0,str2[i])

    print("".join(str1))    
