class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.id_number=idnumber        
    def display(self):
        print("Name:",self.name)
        print("Id number:",self.id_number)

class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idnumber)

a=Employee("Rahul",886012,200000,"Intern")
a.display()
