n = int(input())
max_capcity = 0
passengers_count = 0

for i in range(n):
    a,b = map(int,input().split(" "))
    passengers_count += b
    passengers_count -= a
    if passengers_count > max_capcity:
        max_capcity = passengers_count

print(max_capcity)
