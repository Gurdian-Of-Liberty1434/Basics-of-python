#Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.

elec=int(input("Enter the amount of units consumed"))

if elec<50:
    amount=elec*2.60
    tax=25
elif elec<100:
    amount=130+(elec-50)*3.25
    tax=35
elif elec<200:
    amount=130+160.5+(elec-100)*5.26
    tax=45
else:
    amount=130+160.5+526+(elec-200)*8.45
    tax=75
total=tax+amount
print("The total amount is",total)