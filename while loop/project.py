
num=int(input("Enter a number"))
digit=0
while num>0:
    num=num//10
    digit=digit+1
print("The number of digits are", digit)