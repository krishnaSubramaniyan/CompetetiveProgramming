from functools import reduce
import operator
for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    index = arr.index(min(arr))
    arr[index] += 1
    print(reduce(operator.mul, arr))
    
