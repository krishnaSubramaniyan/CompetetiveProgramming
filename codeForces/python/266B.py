n,t = map(int,input().split(" "))
q = [i for i in input()]

if n > 1:
    for _ in range(t):
        i = 0;
        while (i < n-1):
            if (q[i] == 'B') and (q[i+1] == 'G'):
                q[i] = 'G'
                q[i+1] = 'B'
                i += 2
            else:
                i += 1

    print(''.join(q))
else:
    print(q[0])
