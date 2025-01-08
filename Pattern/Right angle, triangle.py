#Write a program to demonstrate a right angle triangle pattern?
row=int(input("Enter the number of rows you want"))
for i in range(row):
    for p in range(i+1):
        print("*", end=" ")

    print( )