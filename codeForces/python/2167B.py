def count_char(s) -> dict:
    temp = dict()
    for c in s:
        if not temp.get(c):
            temp[c] = 1
        else:
            temp[c] += 1
    return temp

for _ in range(int(input())):
    n = input()
    s = input().split()
    
    a,b = count_char(s[0]), count_char(s[1])
    for k in a.keys():
        try:
            if a[k] != b[k]:
                print("NO")
                break
        except:
            print("NO")
            break
    else:
        print("YES")
        
        
