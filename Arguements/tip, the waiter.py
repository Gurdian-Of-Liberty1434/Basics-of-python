def total_calc(bill, tip_perc):
    amount=bill*(1+0.01*tip_perc)
    print("Total bill amount", amount)

amount=int(input("Enter total amount "))
tip_perc=int(input("Enter percent as a tip "))
total_calc(amount, tip_perc)
