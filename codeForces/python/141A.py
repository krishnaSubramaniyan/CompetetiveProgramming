def symmetric_difference(l1 :list, l2 :list) -> list:
    pointer = 0
    for _ in range(len(l2)):
        try:
            l2.pop(l2.index(l1[pointer]))
            l1.pop(pointer)
        except:
            pointer += 1

    l1.extend(l2)
    return l1


s1,s2,s3 = [input() for i in range(3)]

if symmetric_difference(list(s1+s2),list(s3)) == []:
    print("YES")
else:
    print("NO")
