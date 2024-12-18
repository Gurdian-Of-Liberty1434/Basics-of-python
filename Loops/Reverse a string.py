#Write a program to reverse the string entered by the user.
text=input("Enter a word")
m=("")

for i in text:
    m=i+m
    
print("The original string is",text)
print("The reverse string is", m)