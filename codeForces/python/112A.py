str1 = input().lower()
str2 = input().lower()

alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

result = 0
for i in range(len(str1)):
    if str1[i] == str2[i]:
        continue
    elif alphabet.index(str1[i],0,27) > alphabet.index(str2[i],0,27):
        result = 1
        break
    else:
        result = -1
        break

print(result)
