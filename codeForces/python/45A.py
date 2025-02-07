monthList = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December")

pointer = monthList.index(input())
for i in range( int(input()) ):
    if(pointer == 11 ):
        pointer = 0
        continue
    pointer += 1

print(monthList[pointer])
