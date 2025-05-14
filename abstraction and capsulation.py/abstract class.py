from abc import ABC, abstractmethod
class base(ABC):
    def print(self,x):
        print("Passed value:",x)
    @abstractmethod
    def task(self):
        print("We are inside Abstract method!")    
class test_class(base):
    def task(self):
        print("We are inside test_class class!")
test_obj=test_class()
test_obj.task()
test_obj.print(100)