l = int(input())
s = input()

if l == 1:
    print(0)
else:
    pointer,remove = 0,0
    for i in range(l-1):
        if s[pointer] != s[i+1]:
            pointer = i+1
        else:
            remove += 1
    print(remove)
