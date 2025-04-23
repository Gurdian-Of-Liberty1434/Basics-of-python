#Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented
class employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor created")

def Create_object():
    print("Creating object...")
    obj=employee()
    print("Function ended...")
    return obj

print("Calling function Create_object()...")
obj=Create_object()
print("Program ended...")
