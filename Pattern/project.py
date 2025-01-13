row=int(input("Enter the number of rows you want"))
for i in range(row):
    for p in range(row-i):
        print(" ", end=" ")
    for q in range(i+1):
        print("*", end=" ")
    print( )
