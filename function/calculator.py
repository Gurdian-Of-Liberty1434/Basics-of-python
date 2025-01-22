#Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.

def add(q,w):
    return q+w

def subtract(q,w):
    return q-w

def multiply(q,w):
    return q*w

def divide(q,w):
    return q/w

print("Please select the operation.\n a.Add \n b.Subtract \n c.Multiply \n d. Divide")

choice=input("Enter the operation : ")

num1=int(input("Enter the 1st number : "))

num2=int(input("Enter the 2nd number : "))


if choice=="a":
    print("The addition of two numbers is :",add(num1,num2))
elif choice=="b":
    print("The subtraction of two numbers is :",subtract(num1,num2))
elif choice=="c":
    print("The multiplication of two numbers is :",multiply(num1,num2))
elif choice=="d":
    print("The division of two numbers is :",divide(num1,num2))