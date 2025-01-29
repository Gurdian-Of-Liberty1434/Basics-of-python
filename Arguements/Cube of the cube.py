def cube_find(cube_number):
    c=cube_number**3
    print(c)
cube_number=int(input("Enter a cube number "))
if cube_number%3==0:
    cube_find(cube_number)
else:
    print("The number isn't divisible by 3")