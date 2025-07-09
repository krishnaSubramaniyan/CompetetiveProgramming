n = int(input())
available = 0

for _ in range(n):
    p,q = map(int, input().split())
    if (q-p) > 1:
        available += 1

print(available)
