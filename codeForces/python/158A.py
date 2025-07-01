n,k = [ int(i) for i in input().split(" ")]
scores = [ int(i) for i in input().split(" ")]
k = scores[k-1]

count = 0
for i in range(n):
    if scores[i] != 0 and scores[i] >= k:
        count += 1
    else:
        break
print(count)
