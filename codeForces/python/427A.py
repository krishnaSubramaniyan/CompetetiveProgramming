plice_count,crime_count = 0,0
input()
for i in map(int, input().split()):
    if i > 0:
        plice_count += i
    elif (i == -1) and (plice_count > 0):
        plice_count -= 1
    else:
        crime_count += 1    

print(crime_count)
