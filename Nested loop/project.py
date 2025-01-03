num=int(input("Enter a number"))
binary=0
i=1
while num>0:
    rem=num%2
    binary=binary+rem*i
    num=num//2
    i=i*10
print(binary)