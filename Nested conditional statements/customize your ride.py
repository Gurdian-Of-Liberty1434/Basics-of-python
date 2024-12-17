print('Select ur ride:')
print('1. Bike')
print('2. car')
ans=int(input("Enter your choice:"))
if ( ans==1 ):
    print('What type of bike?')
    print("1.Scooter")
    print('2.Scooty')
    ans2=int(input("Enter another choice:"))
    if ( ans2==1 ):
        print("Scooter selected")
    else:
        print("Scooty selected")
elif ( ans==1 ):
    print('What type of car?')
    print("1.Sedan")
    print('2.Hatchback')
    ans3=int(input("Enter another choice:"))
    if ( ans3==1 ):
        print("Sedan selected")
    else:
        print("Hatchback selected")