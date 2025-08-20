for _ in range(int(input())):
    count = 0
    s = input()
    v = "codeforces"
    for i in range(10):
        if s[i] != v[i]:
            count += 1

    print(count)
