string = input()
length = len(string)
if length > 2:
    distinct_letters = set(string[1:length-1].split(", "))
    print(len(distinct_letters))
else:
    print(0)
