#write a program to demonstrate the numbers in a diamond pattern
row=int(input("Enter the number of rows you want"))
if row%2==0:
    half=int(row/2)
else:
    half=int(row/2)+1
for i in range(1,half+1):
    for p in range(half-i):
        print(" ", end=" ")
    for q in range(2*i-1):
        print("*", end=" ")
    print( )
for i in range(half,0,-1):
    for p in range(half-i):
        print(" ", end=" ")
    for q in range(2*i-1):
        print("*", end=" ")
    print( )


