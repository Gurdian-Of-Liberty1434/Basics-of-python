#Write a program to calculate the BMI of a person?elif
weight=float(input("Enter ur weight in kg"))
height=float(input("Enter ur height in m"))

bmi= weight/(height*height)


if bmi<=18.4:
    print("TOO SKINNY, EVEN AN ANT CAN KILL U")

elif bmi<=24.9:
    print("U r just a regular guy, don't think u r special")
elif bmi<=29.9:
    print("U R ABOUT THE SIZE OF AN ELEPHANT")
elif bmi<=34.9:
    print("OMG, U R ANOTHER PLANET, PLS DONT CRUSH ME")
else:
    print("OMG, WE R IN HELL, DONT BURN ME PPLLSSSSSSSSSSSSSSSS")