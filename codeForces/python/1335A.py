for i in range(int(input())):
    candies = int(input())
    if candies > 2:
        if candies%2==1:
            print(candies//2)
        else:
            print(int(candies/2 - 1))
    else:
        print(0)
