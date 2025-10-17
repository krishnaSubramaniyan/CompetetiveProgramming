for _ in range(int(input())):
    s = input()
    l = len(s)
    if l > 1:
        half = l//2
        if (s[:half]) == (s[half:]):
            print("YES")
            continue
    print("NO")
