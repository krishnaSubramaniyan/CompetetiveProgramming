n = int(input())
index = (0, 2, 4)
result = 0
for i in range(n):
    answer = input()
    know_answer = 0
    for i in index:
        if answer[i] == '1':
            know_answer += 1
    if know_answer > 1:
        result += 1

print(result)
