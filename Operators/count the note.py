#Write a program to calculate the number of notes in the given amount?
a=int(input("Enter the amount-")) #converting the string into integer by using int


note1=a//100

note2=(a%100)//50

note3=((a%100)%50)//10
print("The number of 100s are:",note1)
print("The number of 50s are:",note2)
print("The number of 10s are:",note3)