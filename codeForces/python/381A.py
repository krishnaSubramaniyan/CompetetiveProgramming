scores = [0,0]
n = int(input())
cards = list(map(int, input().split()))

for i in range(n):
    player = i%2
    if cards[0] >= cards[-1]:
        scores[player] += cards[0]
        cards.pop(0)
    else:
        scores[player] += cards[-1]
        cards.pop(-1)

print(f'{scores[0]} {scores[1]}')
