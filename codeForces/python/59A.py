s = input()
upper_count, lower_count = 0,0

for i in s:
    if i.isupper():
        upper_count += 1
    else:
        lower_count += 1

if (upper_count == lower_count) or (lower_count > upper_count):
    print(s.lower())
else:
    print(s.upper())
