result = []

for _ in range(int(input())):
    rank = int(input())

    if rank <= 1399:
        result.append(4)
    elif rank <= 1599:
        result.append(3)
    elif rank <= 1899:
        result.append(2)
    else:
        result.append(1)

for i in result:
    print(f"Division {i}")
