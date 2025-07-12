a = int(input(),2) # convert base 2 binary
b = input()
l = len(b)
b = int(b, 2)

xor = a^b

print(f'{xor:0{l}b}') #0{l} -> length maintain, b -> convert binary
