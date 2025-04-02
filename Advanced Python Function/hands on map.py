#Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
number1=[1,2,3]
number2=[4,5,6]
result=list(map(lambda x,y:x+y,number1,number2))
print(list(result))

nums=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,nums))
print(square)