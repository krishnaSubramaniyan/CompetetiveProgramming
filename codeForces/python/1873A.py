for _ in range(int(input())):
    s = input()
    if s == "abc" or ( (s[2]+s[1]+s[0] == "abc") or (s[1]+s[0]+s[2] == "abc") or (s[0]+s[2]+s[1] == "abc")):
        print("YES")
    else:
        print("NO")
