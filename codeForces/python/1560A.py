t = []
for _ in range(int(input())):
    t.append(int(input()))

end = max(t)

arr = []
i = 1
c = 3
l = 0
while end >= l:
    if (i == c):
        c += 10
    elif (i%3 != 0):
        arr.append(i)
        l += 1
    i += 1

for i in t:
    print(arr[i-1])
