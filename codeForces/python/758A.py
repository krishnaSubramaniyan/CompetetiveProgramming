result = 0
input()
arr = list(map(int, input().split()))
m = max(arr)
for i in arr:
    if i < m:
        result += m-i

print(result)
