Valid=False

while not Valid:
    try:
        n=int(input("Enter a number: "))

        while n%2==0:
            print("bye")
        Valid=True
    except ValueError:
        print("Invalid")