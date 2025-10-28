def ascii_add(s):
    temp = 0
    for c in s:
        temp += ord(c)
    return temp

for _ in range(int(input())):
    input()
    s = input().split()
    if ascii_add(s[0]) == ascii_add(s[1]):
        print("YES")
    else:
        print("NO")
    
