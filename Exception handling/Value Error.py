try:
    a=int(input("Enter a number "))
    print(a)
except ValueError as ex:
    print("ERROR!",ex)