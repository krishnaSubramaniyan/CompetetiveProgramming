for _ in range(int(input())):
    swap_count = 0
    n = int(input())
    arr = list(map(int, input().split()))
    position = [[0],[0]] #indice 0 - even number, 1 - odd number

    for i in range(n):
        mod = i%2
        if mod != arr[i]%2:
            position[mod].append(i)
            position[mod][0] += 1
        if (position[0][0] > 0) and (position[1][0] > 0):
            a = position[0].pop()
            b = position[1].pop()
            arr[a],arr[b] = arr[b],arr[a]
            position[0][0] -= 1
            position[1][0] -= 1
            swap_count += 1

    if (position[0][0] > 0) or (position[1][0] > 0):
        print(-1)
    else:
        print(swap_count)
