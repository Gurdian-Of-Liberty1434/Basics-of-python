#Write a program to demonstrate a Floyd triangle pattern?
rows=int(input("Enter the number of rows you want"))
num=1
for i in range(1, rows+1):
    for p in range(1,i+1):
        print(num, end=" ")
        num=num+1
    print( )