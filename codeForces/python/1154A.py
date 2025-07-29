numbers = list(map(int, input().split()))

sum_value = max(numbers)
numbers.pop(numbers.index(sum_value))
for i in numbers:
    print(sum_value - i, end=" ")
