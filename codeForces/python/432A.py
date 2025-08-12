n,k = map(int, input().split())
p = [ i for i in map(int, input().split()) if(i+k<6)]

print(len(p)//3)
