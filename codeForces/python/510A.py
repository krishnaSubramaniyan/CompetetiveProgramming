r,c = map(int, input().split())
dot_str = '.'*(c-1)
hast_str = '#'*c
for i in range(1,r+1):
    if i%2==1:
        print(hast_str)
    else:
        if (i/2)%2==1:
            print(dot_str+"#")
        else:
            print("#"+dot_str)
