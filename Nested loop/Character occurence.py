#Write a program to check how many times a character is repeated in a word?
text=input("Enter a word")
character=input("Which character you wanna search")

i=0
count=0
while i<len(text):
    if text[i]==character:
        count=count+1
    i=i+1
    
print("The total number of times", character,"is occuring is",count )   
#the total number of times n is occuring is 2 