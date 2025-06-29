for i in range(int(input())):
    word = input()
    length = len(word)
    if length>10:
        print(word[0]+str(length-2)+word[-1])
    else:
        print(word)
