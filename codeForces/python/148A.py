damaged_dragons = 0
k,l,m,n,d = [int(input()) for _ in range(5)]

for i in range(1,d+1):
    if not(i%k) or not(i%l) or not(i%m) or not(i%n):
        damaged_dragons += 1

print(damaged_dragons)
