n = int(input())
scores = [ int(i) for i in input().split(" ") ]
performance_count = 0

if n > 1:
    last_worst_score, last_best_score = scores[0], scores[0]
    for i in range(1,n):
        
        if scores[i] < last_worst_score:
            performance_count += 1
            last_worst_score = scores[i]
        elif scores[i] > last_best_score:
            performance_count += 1
            last_best_score = scores[i]

print(performance_count)
