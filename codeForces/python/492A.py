i,row,used = 0,0,0
cubes = int(input())
while True:
    i += 1
    used += i
    cubes -= used
    if cubes > -1:
        row += 1
    else:
        break
print(row)
