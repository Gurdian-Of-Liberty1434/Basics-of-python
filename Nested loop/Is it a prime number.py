#Write a program to print all the prime numbers which come in the range entered by the user?
mini=int(input("Enter the minimum number"))
max=int(input("Enter the maximum number"))

for i in range(mini, max+1):
    if i>1:
        for x in range(2,i):
            if i%x==0:
                break
        else:
            print(i)


