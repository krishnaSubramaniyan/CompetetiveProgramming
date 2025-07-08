s = input()
t = input()

def birlandish(s,t) -> bool:

    if len(s) != len(t):
        return False

    length = len(s)-1
    for i in range(len(s)):
        if s[i] != t[length-i]:
            return False

    return True

if birlandish(s,t):
    print("YES")
else:
    print("NO")

