for _ in range(int(input())):
    count = 0
    solved = []
    input()
    for i in input():
        if i in solved:
            count += 1
        else:
            solved.append(i)
            count += 2
    print(count)
