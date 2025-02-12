try:
    num1,num2=eval(input("Enter two numbers, seperated by a comma"))
    result = num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("ERROR! ZERO IS UNDIVISIBLE")

except SyntaxError:
    print("ERROR! COMMA MISSING")

except:
    print("WRONG INPUT")

else:
    ("ERROR! NO EXCEPTIONS")

finally:
    print("This will execute, no matter what")