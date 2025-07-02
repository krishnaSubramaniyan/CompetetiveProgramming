r,c,move = 0,0,0

def move_one(pos):
    global move
    if pos > 2:
        for _ in range(2):
            if pos != 2:
                pos -= 1
                move += 1
            else:
                break
    else:
        for _ in range(2):
            if pos != 2:
                pos += 1
                move += 1
            else:
                break
            
# INPUT
for i in range(0,5):
    column = input().split(" ")
    if '1' in column:
        c = column.index("1",0,5)
        r = i

if (r != 2):
    move_one(r)
if (c != 2):
    move_one(c)

# RESULT
print(move)
