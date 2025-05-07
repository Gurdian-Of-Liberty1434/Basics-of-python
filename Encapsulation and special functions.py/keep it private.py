class myClass:
   __privatevar=27
   def __privMeth(self):
      print("I'm inside class myClass")
   def hello(self):
      print("Private variable is",myClass.__privatevar)

foo=myClass()
foo.hello()
foo.__privMeth()