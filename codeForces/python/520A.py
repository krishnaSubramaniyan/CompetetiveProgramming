input()
pangram = set(input().lower())

if len(pangram) > 25:
    print("YES")
else:
    print("NO")
