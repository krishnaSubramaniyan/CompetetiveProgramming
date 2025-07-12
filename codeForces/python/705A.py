msg = ('I love that ', 'I hate that ')
n = int(input())

for i in range(1,n):
    print(msg[i%2],end="")

if n%2 == 0:
    print('I love it')
else:
    print('I hate it')
